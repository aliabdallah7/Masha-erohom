

const form = document.getElementById('emotionForm');
const emojiContainer = document.getElementById('emoji-container');

form.addEventListener('submit', (event) => {
    event.preventDefault(); 
    const keyword = document.getElementById('text').value;
    fetch('/predict_emotion', {
        method: 'POST',
        body: JSON.stringify({ text: keyword }),
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        const predictedEmotion = data.emotion;
        const emojiContainer = document.getElementById('emojiContainer');
        const emoText = document.getElementById('emoText');
        dict = {'none': 'لا تشعر بشيء', 'anger': 'غاضب','joy':'سعيد','sadness':'حزين','love':'تشعر بالحب','sympathy':'متعاطف او تدعو','surprise':'متفاجئ','fear':'خائف'};
        emoText.textContent = 'انت ' + dict[predictedEmotion]
        const animationPath = `${basePath}${predictedEmotion}.json`;  // Adjust path as needed
        emojiContainer.load(animationPath)
    })
    .catch(error => console.error(error));
});