from slack_bolt import App
import os

# Initialize Slack Bolt for LIGHT Agent
app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

# Slash command renamed to /light
@app.command("/light")
def handle_light(ack, command, client):
    ack("LIGHT is on the case! Working on your request...")
    user_id = command["user_id"]
    text = command.get("text", "")
    # TODO: call orchestrator.process(user_id, text) and post back

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
