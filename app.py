import streamlit as st

st.title("ไมโครโฟนใน Streamlit")

st.write("คลิกปุ่มด้านล่างเพื่อเริ่มบันทึกเสียงจากไมโครโฟนและแปลงเป็นข้อความ")

mic_script = """
<script>
    var recognition;

    function startRecording() {
        recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'th-TH';
        recognition.continuous = true;
        recognition.interimResults = false;

        recognition.onresult = function(event) {
            var transcript = event.results[0][0].transcript;
            console.log(transcript);
            
            document.getElementById('transcript').value = transcript;
        };

        recognition.start();

        document.getElementById('stopButton').style.display = 'block';
        document.getElementById('startButton').style.display = 'none';
    }

    function stopRecording() {
        recognition.stop();
        document.getElementById('stopButton').style.display = 'none';
        document.getElementById('startButton').style.display = 'block';
    }
</script>
<button id="startButton" onclick="startRecording()">เริ่มพูด</button>
<button id="stopButton" onclick="stopRecording()" style="display:none;">หยุดพูด</button>
<input id="transcript" style="width: 100%;" readonly></input>
"""

st.components.v1.html(mic_script, height=200)


