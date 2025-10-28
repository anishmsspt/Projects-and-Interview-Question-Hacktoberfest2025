const QRinput = document.getElementById('qr-input');
const GenerateQRbtn = document.getElementById('generate-button');
const QRcodeContainer = document.getElementById('qr-code');
const downloadBtn = document.getElementById('download-button');

GenerateQRbtn.addEventListener('click', () => {
    const inputValue = QRinput.value.trim();
    if (!inputValue) {
        alert('Please enter a value to generate a QR code.');
        return;
    }

    // Clear previous QR code
    QRcodeContainer.innerHTML=" "

    QRCode.toCanvas(
        inputValue,
        {
            width: 250,
            margin: 2,
            color: {
                dark: '#000000',
                light: '#ffffff'
            }
        },
        (err,canvas)=>{
            if(err){
                alert("Error in generating QR code");
            }
            if(canvas){
                QRcodeContainer.appendChild(canvas);
                downloadBtn.style.display = 'inline-block';
            }
        }
    )
    
})

//Download QR code
downloadBtn.addEventListener('click', () => {
    const canvas = QRcodeContainer.querySelector('canvas');
    console.log(canvas);
    if(canvas){
        const dataUrl = canvas.toDataURL('image/png')
        const a = document.createElement('a')
        a.href = dataUrl
        a.download = "qrCode.png"
        a.click()
    }
})