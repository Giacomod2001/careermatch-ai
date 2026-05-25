import os

gdpr_path = "shared_core/gdpr_compliance.py"
with open(gdpr_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_privacy_page = False

for line in lines:
    if line.startswith("def render_privacy_policy_page():"):
        in_privacy_page = True
        new_lines.append(line)
        continue
        
    if in_privacy_page and line.startswith("def render_ai_transparency()"):
        in_privacy_page = False
        new_lines.append(line)
        continue

    if in_privacy_page:
        # We need to restructure the layout from line 431 "st.divider()"
        # The structure is:
        # st.divider()
        # # --- PRIVACY POLICY SECTIONS ---
        # st.markdown(f"## {_t('privacy_heading')}")
        # ...
        # st.divider()
        # # --- AI TRANSPARENCY ---
        # ...
        if "st.divider()" in line and "# --- PRIVACY POLICY SECTIONS ---" in "".join(lines[lines.index(line)+1:lines.index(line)+2]):
            # This is the start! We replace from here.
            # We don't append st.divider()
            pass
        elif "# --- PRIVACY POLICY SECTIONS ---" in line:
            new_lines.append("    left_menu, right_content = st.columns([1, 3])\n")
            new_lines.append("    with left_menu:\n")
            new_lines.append("        st.markdown(\"<h4 style='color: #00A0DC; margin-bottom: 1rem;'>Legal Menu</h4>\", unsafe_allow_html=True)\n")
            new_lines.append("        selected_section = st.radio(\"Legal Menu\", [_t('privacy_heading'), _t('ai_heading'), _t('exercise_rights')], label_visibility=\"collapsed\")\n")
            new_lines.append("\n    with right_content:\n")
            new_lines.append("        if selected_section == _t('privacy_heading'):\n")
            new_lines.append("        " + line) # Indent the comment
        elif "st.markdown(f\"## {_t('privacy_heading')}\")" in line:
            new_lines.append("            st.markdown(f\"## {_t('privacy_heading')}\")\n")
        elif "st.divider()" in line:
            # Skip dividers inside the blocks
            pass
        elif "# --- AI TRANSPARENCY ---" in line:
            new_lines.append("        elif selected_section == _t('ai_heading'):\n")
            new_lines.append("        " + line)
        elif "# --- EXERCISE RIGHTS ---" in line:
            new_lines.append("        elif selected_section == _t('exercise_rights'):\n")
            new_lines.append("        " + line)
        elif "st.markdown(f\"## {_t('ai_heading')}\")" in line:
            new_lines.append("            st.markdown(f\"## {_t('ai_heading')}\")\n")
        elif "st.markdown(f\"## {_t('exercise_rights')}\")" in line:
            new_lines.append("            st.markdown(f\"## {_t('exercise_rights')}\")\n")
        else:
            # We must indent all other lines by 8 spaces (since they were indented by 4 spaces originally, and now they are inside `with right_content:` -> `if selected_section == ...:` which requires 12 spaces).
            # Originally they were 4 spaces. So add 8 spaces.
            leading = len(line) - len(line.lstrip())
            if leading >= 4 and not line.strip() == "":
                new_lines.append("        " + line)
            else:
                new_lines.append(line)
    else:
        new_lines.append(line)

with open(gdpr_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Privacy UI refactored.")
