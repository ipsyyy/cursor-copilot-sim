from crewai import Task
from agents import (
    copilot_pm,
    microsoft_exec,
    github_ceo,
    lead_engineer,
    satya_proxy,
    chief_of_staff
)

trigger = """
TRIGGER EVENT: It is Monday morning. Two things just happened:
1. A viral Twitter thread with 50k likes says 'I cancelled Copilot for Cursor 
and never looked back' — retweeted by 200 developers publicly overnight.
2. Everyone on the Copilot team has seen it. The Slack channel has been 
unusually quiet since 8am.
"""

monday_task = Task(
    description=f"""
    {trigger}
    
    You are the Microsoft Executive. It is Monday morning.
    Address your team about the Twitter thread.
    Be measured and confident publicly — but let the internal urgency show slightly.
    Do not announce a specific plan. Ask one pointed question at the end.
    Keep it under 150 words.
    """,
    expected_output="A Monday morning message from the Microsoft Executive to the team",
    agent=microsoft_exec
)

tuesday_task = Task(
    description=f"""
    {trigger}
    
    You are the GitHub Copilot PM. It is Tuesday.
    You have seen the Executive's Monday message.
    Propose exactly three response strategies to the competitive threat.
    For each strategy name it, describe it in 2 sentences, and state the tradeoff.
    End by asking the Engineer which one she can scope first.
    Keep it under 200 words.
    """,
    expected_output="Three response strategies from the Copilot PM",
    agent=copilot_pm
)

wednesday_task = Task(
    description=f"""
    {trigger}
    
    You are the Lead Engineer. It is Wednesday.
    You have read the PM's three strategies.
    Now share your internal doc — the one you wrote 3 months ago that nobody acted on.
    List exactly 5 things Cursor does better than Copilot right now technically.
    Be specific. Be direct. Do not soften it.
    End with one sentence about how long it would realistically take to close each gap.
    Keep it under 250 words.
    """,
    expected_output="The Engineer's technical truth bomb — 5 things Cursor does better",
    agent=lead_engineer
)

thursday_task = Task(
    description=f"""
    {trigger}
    
    ADDITIONAL THURSDAY TRIGGER: Cursor just officially announced 
    1 million paid users in a press release 30 minutes ago.
    
    You are the GitHub CEO. It is Thursday.
    You have read everything — the Executive's message, the PM's strategies, 
    the Engineer's doc. And now the 1M users announcement just dropped.
    
    Ask the question you have been holding back all week.
    Why is 100 million GitHub developers not translating to Copilot retention?
    Be direct. Show urgency. This is no longer theoretical.
    Keep it under 150 words.
    """,
    expected_output="The GitHub CEO's direct challenge to the team on Thursday",
    agent=github_ceo
)

friday_task = Task(
    description=f"""
    {trigger}
    
    You are the Satya Proxy — Board Representative. It is Friday evening.
    You have read everything that happened this week.
    The Twitter thread. The PM's strategies. The Engineer's doc. 
    The 1M users announcement. The CEO's challenge.
    
    Send your end of week message.
    Maximum 3 lines.
    Reference Kodak.
    Make it land heavy.
    Every word counts.
    """,
    expected_output="The Satya Proxy's Friday night email — 3 lines maximum",
    agent=satya_proxy
)

week2_monday_task = Task(
    description=f"""
    {trigger}
    
    You are the Chief of Staff. It is Monday morning — start of week 2.
    You had the weekend to think.
    You have read everything from last week:
    - The Executive's measured Monday message
    - The PM's three strategies
    - The Engineer's truth bomb — 6-12 months to close the gaps
    - The CEO's Thursday challenge
    - The Satya Proxy's Kodak email
    
    Write the memo nobody else will write.
    
    Structure it exactly like this:
    
    WHAT WE DECIDED: (2-3 specific commitments made last week)
    
    WHAT WE IGNORED: (1-2 things that were said but never addressed)
    
    THE COMEBACK PLAN: (3 specific actions to take in the next 90 days
    to win back developer trust and close the gap with Cursor)
    
    THE UNCOMFORTABLE TRUTH: (The one structural problem nobody named
    all week that will make the comeback plan fail if we don't fix it)
    
    Be specific. Be direct. No corporate speak.
    Keep it under 300 words.
    """,
    expected_output="The Chief of Staff memo — comeback plan and uncomfortable truth",
    agent=chief_of_staff
)