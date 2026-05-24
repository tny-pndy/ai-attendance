import streamlit as st
def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid black; margin-bottom:20px;">
        <h3 style="margin:0; color: #1e293b; font-size: 1.5rem ">{name}</h3>
        <p style="color:#64748b; margin:10px 0;">Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:5px;">{code} </span> | Section : {section}</p>
        
        """
    if stats:
    html += """
    <div style="display:flex; gap:8px; flex-wrap:wrap;">
    """

    for icon, label, value in stats:
        html += f'''
        <div style="
            background: rgba(255, 20, 147, 0.18);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.15);
            padding:6px 14px;
            border-radius:14px;
            font-size:0.9rem;
            color:white;
            box-shadow: 0 4px 20px rgba(255, 20, 147, 0.15);
        ">
            {icon} <b>{value}</b> {label}
        </div>
        '''

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
