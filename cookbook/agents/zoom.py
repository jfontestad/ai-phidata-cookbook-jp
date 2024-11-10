"""
Demonstration of Zoom meeting auto-scheduling agent

This script demonstrates the implementation of an agent that uses the Zoom API to automatically schedule meetings and manage meeting details.

Required environment variables:
ZOOM_ACCOUNT_ID: Zoom account ID
ZOOM_CLIENT_ID: Zoom client ID
ZOOM_CLIENT_SECRET: Zoom client secret

Main features:
Automatic scheduling of Zoom meetings
Acquisition and display of meeting details
Error handling
"""

Importing required libraries
import os
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.zoom import ZoomTool

Get Zoom API authentication information
ACCOUNT_ID = os.getenv("ZOOM_ACCOUNT_ID")
CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")

Define custom Zoom tool class
class CustomZoomTool(ZoomTool):
def schedule_meeting(self, topic: str, start_time: str, duration: int) -> str:
"""
Schedules a meeting and returns formatted details

    Parameters:
    topic (str): Meeting topic
    start_time (str): Start time (ISO 8601 format)
    duration (int): Duration (min)

    Returns:
    str: Formatted meeting information
    """
    response = super().schedule_meeting(topic, start_time, duration)

    if isinstance(response, str):
        import json
        try:
            meeting_info = json.loads(response)
        except json.JSONDecodeError:
            return "Failed to parse meeting info."
        else:
            meeting_info = response
    
    if meeting_info:
        meeting_id = meeting_info.get("id")
        join_url = meeting_info.get("join_url")
        start_time = meeting_info.get("start_time")
        return (
            f"Meeting successfully scheduled!\n\n"
            f"**Meeting ID:** {meeting_id}\n"
            f"**Join URL:** {join_url}\n"
            f"**Start time:** {start_time}"
        )
    else:
        return "Sorry, failed to schedule meeting."

Instantiate Zoom tool
zoom_tool = CustomZoomTool(
account_id=ACCOUNT_ID,
client_id=CLIENT_ID,
client_secret=CLIENT_SECRET
)

Scheduling agent configuration
agent = Agent(
name="Zoom Scheduling Agent",  # Agent name
agent_id="zoom-scheduling-agent",  # Agent ID
model=OpenAIChat(id="gpt-4o"),  # Use GPT-4 model
tools=[zoom_tool],  # Use custom Zoom tool
markdown=True,  # Enable markdown output
debug_mode=True,  # Enable debug mode
show_tool_calls=True,  # Enable display of tool calls
instructions=[
"Use the Zoom API as an agent to schedule Zoom meetings.",
"When scheduling a meeting, use the ZoomTool's schedule_meeting function.",
"Unless otherwise specified, pass only the minimum required parameters to the schedule_meeting function.",
"After scheduling, provide details such as the meeting ID, join URL, and start time.",
"Times are all in ISO format. Please specify in 8601 format (e.g. '2024-12-28T10:00:00Z'). ",
"If an error occurs, we will respond appropriately and notify the user. "
],
system_message=(
"Do not change the default parameters of the schedule_meeting function unless explicitly requested by the user. Always make sure the meeting has been successfully scheduled before asking the user."
),
)

Schedule a meeting using an agent
user_input = "Schedule a meeting for 60 minutes on November 1, 2024 at 11:00 AM UTC with the title 'Python Automation Meeting.'"
response = agent.run(user_input)
