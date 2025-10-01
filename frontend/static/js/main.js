const BACKEND_URL = "http://127.0.0.1:5001";

// Visitor API calls
async function approveVisitor(visitorId) {
    const response = await fetch(`${BACKEND_URL}/approveVisitor`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            visitorId: visitorId,
            userId: "resident_001",
            token: "TEST_FCM_TOKEN"
        })
    });
    const data = await response.json();
    document.getElementById("visitor-result").innerText = JSON.stringify(data);
}

async function denyVisitor(visitorId) {
    const reason = prompt("Enter reason for denial");
    if (!reason) return;
    const response = await fetch(`${BACKEND_URL}/denyVisitor`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            visitorId: visitorId,
            userId: "resident_001",
            reason: reason,
            token: "TEST_FCM_TOKEN"
        })
    });
    const data = await response.json();
    document.getElementById("visitor-result").innerText = JSON.stringify(data);
}

// AI Chat
async function sendChat() {
    const prompt = document.getElementById("chat-input").value;
    const response = await fetch(`${BACKEND_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });
    const data = await response.json();
    document.getElementById("chat-output").innerText = JSON.stringify(data, null, 2);
}
