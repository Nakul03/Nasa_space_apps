// static/script.js

document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-button');
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    // Function to append messages to the chat box
    function appendMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        messageDiv.textContent = `${sender === 'user' ? 'You' : 'Bot'}: ${message}`;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Function to send user message
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        appendMessage(message, 'user');
        userInput.value = '';
        sendButton.disabled = true;

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_input: message }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                appendMessage(errorData.response || 'Error occurred.', 'bot');
                return;
            }

            const data = await response.json();
            appendMessage(data.response, 'bot');
        } catch (error) {
            console.error('Error:', error);
            appendMessage('Sorry, something went wrong.', 'bot');
        } finally {
            sendButton.disabled = false;
        }
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});
