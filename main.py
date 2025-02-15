import requests
import streamlit as st
from typing import Optional

BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "<YOUR-FLOW-ID>"
ENDPOINT = "<SET_YOUR_DESIRED_ENDPOINT_NAME>"

TWEAKS = {
  "File-TAhkx": {},
  "SplitText-zimqh": {},
  "AstraDB-VH0Ui": {},
  "ChatInput-CjF0G": {},
  "Prompt-b3lya": {},
  "AstraDB-i9Ac0": {},
  "ParseData-gXVv8": {},
  "ChatOutput-MGRPK": {},
  "Agent-4xKPK": {},
  "OpenAIModel-U97mM": {},
  "SearchComponent-58shL": {}
}

def run_flow(message: str,
  endpoint: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  api_key: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if api_key:
        headers = {"x-api-key": api_key}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("GSTantra")
    st.subheader("Chatbot for accurate GST tax insights")
    with st.form(key="query_form"):
        message = st.text_area("Message", placeholder="Enter your queries here...", height=350, max_chars=25000)
        submit_button = st.form_submit_button("Run Flow")
    if submit_button:
        if not message.strip():
            st.error("Please enter a message ⚠️")
            return
    
        try:
            response = run_flow(message, ENDPOINT, tweaks=TWEAKS)
            result = response.get("outputs", [{}])[0].get("outputs", [{}])[0].get("results", {}).get("message", {}).get("text", "No response found")
            st.markdown("Your results: ")
            st.success(result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()    

