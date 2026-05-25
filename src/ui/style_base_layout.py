import streamlit as st

def style_background_home():
    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(
    135deg,
    #0f0c29 0%,
    #302b63 45%,
    #24243e 100%
    
    );
                }
               

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                 
                    }
                    
        </style>  

                """
            ,unsafe_allow_html=True)
  





def style_background_dashboard():
    st.markdown("""
        <style>

                .stApp {
                  background: linear-gradient(135deg, #E0EAFC, #CFDEF3) !important;
                  
                }
               

        </style>  

                """
            ,unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        
        <style>
        
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
             
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden !important;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
               
            }

            h1 {
                font-family:  'Poppins' !important;
                font-size: 4.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                font-weight: 900 !important;
                
            }
                

            h2 {
                font-family: 'Poppins', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                -webkit-text-fill-color: black !important;
            }
                
            h3, h4, p {
                font-family: 'Poppins', sans-serif;   
                -webkit-text-fill-color: black !important;
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                webkit-text-fill-color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
               
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                webkit-text-fill-color:white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                -webkit-text-fill-color: black !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)



