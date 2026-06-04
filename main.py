import os
from crewai import Crew, Process
from dotenv import load_dotenv
from agents import (
    copilot_pm,
    microsoft_exec,
    github_ceo,
    lead_engineer,
    satya_proxy,
    chief_of_staff
)
from tasks import (
    monday_task,
    tuesday_task,
    wednesday_task,
    thursday_task,
    friday_task,
    week2_monday_task
)

load_dotenv()

crew = Crew(
    agents=[
        microsoft_exec,
        copilot_pm,
        lead_engineer,
        github_ceo,
        satya_proxy,
        chief_of_staff
    ],
    tasks=[
        monday_task,
        tuesday_task,
        wednesday_task,
        thursday_task,
        friday_task,
        week2_monday_task
    ],
    process=Process.sequential,
    verbose=True
)

print("\n" + "="*60)
print("SIMULATION: The week Cursor hit 1M users")
print("Inside the GitHub Copilot team")
print("="*60 + "\n")

result = crew.kickoff()

print("\n" + "="*60)
print("SIMULATION COMPLETE")
print("="*60)
print("\n--- FULL WEEK OUTPUT ---\n")
print(result)

# Save full output to file
with open("simulation_output.txt", "w") as f:
    f.write("CURSOR vs COPILOT SIMULATION\n")
    f.write("The week Cursor hit 1M paid users\n")
    f.write("="*60 + "\n\n")
    f.write("MONDAY - Microsoft Executive:\n")
    f.write(str(crew.tasks[0].output) + "\n\n")
    f.write("TUESDAY - Copilot PM:\n")
    f.write(str(crew.tasks[1].output) + "\n\n")
    f.write("WEDNESDAY - Lead Engineer:\n")
    f.write(str(crew.tasks[2].output) + "\n\n")
    f.write("THURSDAY - GitHub CEO:\n")
    f.write(str(crew.tasks[3].output) + "\n\n")
    f.write("FRIDAY - Satya Proxy:\n")
    f.write(str(crew.tasks[4].output) + "\n\n")

print("\n✅ Output saved to simulation_output.txt")