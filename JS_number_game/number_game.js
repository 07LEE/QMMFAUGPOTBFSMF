
let computerNum = 0;
let playButton = document.getElementById("play-button");
let userInput = document.getElementById("user-input");
let resultArea = document.getElementById("result-area");
let resetButton = document.getElementById("reset-button");
let chances = 5;
let chanceArea = document.getElementById("chance-area")

playButton.addEventListener("click", play);
resetButton.addEventListener("click", reset);

function pickRandomNum() {
    computerNum = Math.floor(Math.random() * 100) + 1;
    console.log(computerNum);
}

function play() {
    console.log("게임 시작");
    
    chances --;
    chanceArea.textContent = `남은 기회 : ${chances}`;
    let userValue = userInput.value;
    if (userValue < computerNum) {
        resultArea.textContent = "Up"
    }
    else if (userValue > computerNum) {
        resultArea.textContent = "Down"
    }
    else {
        resultArea.textContent = "Good"
    }

    if(chances < 1) {
        gameOver = true ;
    }

    if (gameOver == true) {
        playButton.disabled = true;
    }
}

function reset() {
    userInput.value = "";
    pickRandomNum();
    resultArea.textContent = "결과값이 여기 나옵니다"
};

pickRandomNum();