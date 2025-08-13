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

                // setTimeout(() => {
                //     addMessage("This is a sample AI response from North Electric.", "bot-message");
                // }, 500);

                const myHeaders = new Headers();
                myHeaders.append("Content-Type", "application/json");

                const raw = JSON.stringify({
                    "question": msg
                });

                const requestOptions = {
                    method: "POST",
                    headers: myHeaders,
                    body: raw,
                    redirect: "follow"
                };

                fetch("http://localhost:8000/askai", requestOptions)
                .then((response) => response.text())
                .then((result) => {
                    console.log(result);
                    result_json = JSON.parse(result);
                    console.log(result_json);
                    result_answer = result_json.answer;
                    console.log(result_answer);
                    addMessage(result_answer, "bot-message");
                })
                .catch((error) => console.error(error));
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