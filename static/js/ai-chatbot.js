document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const chatInput = document.getElementById("chat-input");
    const chatMessages = document.querySelector(".chat-messages");

    if (chatForm) {
        chatForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const msg = chatInput.value.trim();
            if (msg) {
                addMessage(msg, "user-message");
                chatInput.value = "";
                setTimeout(() => {
                    addMessage("This is a sample AI response from North Electric.", "bot-message");
                }, 500);
            }
        });
    }

    function addMessage(text, className) {
        const div = document.createElement("div");
        div.classList.add("chat-message", className);
        div.textContent = text;
        chatMessages.appendChild(div);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});