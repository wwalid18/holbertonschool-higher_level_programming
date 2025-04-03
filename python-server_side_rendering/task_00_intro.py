import os

def generate_invitations(template, attendees):
    """Generates personalized invitation files from a template and a list of attendees."""
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Handle empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        invitation_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            invitation_content = invitation_content.replace(f'{{{key}}}', attendee.get(key, "N/A") or "N/A")
        
        # Write to output file
        file_name = f'output_{idx}.txt'
        with open(file_name, 'w') as file:
            file.write(invitation_content)
        print(f'Generated: {file_name}')
