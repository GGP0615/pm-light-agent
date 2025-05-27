import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from backend.orchestrator import process

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

@app.command("/light")
def light_command(ack, body, respond):
    ack()
    user = body["user_id"]
    text = body.get("text", "")
    result = process(user, text)
    respond(result)

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
