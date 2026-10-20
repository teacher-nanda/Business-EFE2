# -*- coding: utf-8 -*-
"""Homework: practice with an AI tutor (copy-and-paste prompt). Returns slide HTML; the caller registers it."""
import html as _h

def prompt_text(topic, target, first):
    return (
        "You are my friendly business English tutor. I am an intermediate (B1) learner and I use American English.\n"
        "Today we are practicing: %s.\n"
        "Rules:\n"
        "1. Ask me ONE question at a time about my real work life. Use this language in your questions: %s.\n"
        "2. Wait for my answer. Never answer for me.\n"
        "3. After each answer, show my sentence and a corrected version, explain the mistake in one short sentence, and give me one more natural way to say it.\n"
        "4. Keep the conversation going with a follow-up question.\n"
        "5. After 6 questions, give me feedback: 3 things I did well, 3 things to improve, and a mini-quiz of 3 sentences to correct.\n"
        "Start now. Your first question: %s" % (topic, target, first))

def ai_slide(banner_html, sid, topic, target, first, bring):
    p = prompt_text(topic, target, first)
    steps = [("1", "Open an AI chat", "Use any AI assistant you like, on your phone or computer."),
             ("2", "Copy the prompt", "Press the button below, paste it into the chat, and send it."),
             ("3", "Answer in English", "Type your answers, or use voice. Write full sentences."),
             ("4", "Collect your corrections", bring)]
    st = ''.join('<div class="ai-step"><span class="ai-n">%s</span><b>%s</b><span>%s</span></div>' % s for s in steps)
    return '''<div class="slide" id="%s">
  %s
  <div class="slide-main"><div class="content">
    <h2>Practice with AI</h2>
    <p class="instruction">Copy the prompt, paste it into an AI chat, and practice. The AI will correct you and give feedback.</p>
    <div class="ai-steps">%s</div>
    <div class="ai-prompt-wrap">
      <div class="ai-prompt-head"><span>Prompt for your AI tutor</span><button class="btn-deal ai-copy" onclick="copyPrompt('%s')">Copy prompt</button></div>
      <pre class="ai-prompt" id="%s-text">%s</pre>
    </div>
  </div></div>
</div>''' % (sid, banner_html, st, sid, sid, _h.escape(p))
