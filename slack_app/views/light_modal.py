# (Optional) Slack modal definition for multi-step input
def build_modal(trigger_id):
    return {
        "trigger_id": trigger_id,
        "view": {
            "type": "modal",
            "title": {"type": "plain_text", "text": "LIGHT Action"},
            "blocks": [
                {"type": "input", "block_id": "input1", "label": {"type": "plain_text", "text": "Query"},
                 "element": {"type": "plain_text_input", "action_id": "user_query"}}
            ],
            "submit": {"type": "plain_text", "text": "Send"}
        }
    }
