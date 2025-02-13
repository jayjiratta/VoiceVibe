let mediaRecorder;
let audioChunks = [];

document.getElementById("recordButton").addEventListener("click", async function () {
    if (!mediaRecorder || mediaRecorder.state === "inactive") {
        let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = []; // ล้างข้อมูลเก่า

        mediaRecorder.ondataavailable = event => audioChunks.push(event.data);
        mediaRecorder.onstop = async () => {
            let audioBlob = new Blob(audioChunks, { type: "audio/wav" });
            let audioUrl = URL.createObjectURL(audioBlob);

            // 🎵 แสดงปุ่มเล่นเสียง
            let audioPlayback = document.getElementById("audioPlayback");
            audioPlayback.src = audioUrl;
            audioPlayback.classList.remove("d-none"); // แสดงเครื่องเล่นเสียง
            audioPlayback.controls = true; // ให้มีปุ่มเล่น

            // 🎤 อัปโหลดไป Flask
            let formData = new FormData();
            formData.append("audio", audioBlob, "recording.wav");

            let response = await fetch("/upload", {
                method: "POST",
                body: formData
            });

            let result = await response.json();
            alert(result.message); // แจ้งผลลัพธ์
        };

        mediaRecorder.start();
        this.textContent = "Stop Recording";
    } else {
        mediaRecorder.stop();
        this.textContent = "Record";
    }
});
