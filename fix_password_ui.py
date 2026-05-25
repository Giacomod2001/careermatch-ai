import os
import re

app_path = "frontend/app.py"
with open(app_path, "r", encoding="utf-8") as f:
    app_content = f.read()

# Fix Dev Console password UI
old_password_ui = """            <div style='background: rgba(13, 17, 23, 0.6); border: 1px solid rgba(0, 160, 220, 0.3); border-radius: 12px; padding: 2.5rem; text-align: center; margin-top: 3rem;'>
                <div style='background: rgba(0, 160, 220, 0.1); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto;'>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00A0DC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                </div>
                <h2 style='margin: 0; color: #E53935;'>System Locked</h2>
                <p style='color: #8b949e; margin-bottom: 2rem;'>Restricted Developer Access Area</p>"""

new_password_ui = """            <div style='border: 1px solid rgba(128, 128, 128, 0.2); border-radius: 12px; padding: 2.5rem; text-align: center; margin-top: 3rem;'>
                <div style='background: rgba(0, 160, 220, 0.1); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem auto;'>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00A0DC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                </div>
                <h2 style='margin: 0; font-weight: 600;'>Developer Authentication</h2>
                <p style='color: gray; margin-bottom: 2rem;'>Please enter the access code to continue</p>"""

app_content = app_content.replace(old_password_ui, new_password_ui)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_content)
print("Dev Console password UI fixed.")

