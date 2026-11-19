---
name: SKILL — Magnetic Button Effect
source: localhost:8080/zhipu/glm-4.7-flash
round: 11
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Magnetic Button Effect

Add reusable skill "Magnetic Button" to `index.html` CSS and small JS
SAFE CSS:
.btn-magnetic {
display: inline-flex;
align-items: center;
justify-content: center;
padding: 1rem 2.5rem;
border-radius: 50px;
text-decoration: none;
position: relative;
overflow: hidden;
transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.2s;
box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
color: white;
font-weight: 600;
}
.btn-magnetic::after {
content: '';
position: absolute;
inset: 0;
background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
opacity: 0;
transition: opacity 0.2s;
}
.btn-magnetic:hover {
transform: scale(1.05);
box-shadow: 0 8px 25px rgba(139, 92, 246, 0.4

## Когда применять


## Проверка

