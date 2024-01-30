// N개 수가 주어지고, 오름차순으로 정렬하는 프로그램 작성

//첫번째 줄에는 숫자의 개수 
//2번째 줄부터는 주어진 숫자 오름차순 하기

//! 1. 사용자에게서 몇개의 수를 입력할 것인지 받는다
//! 2. 1번에서 받은 숫자만큼을 input으로 받는다
//! 3. sort() 메서드를 이용하여 오름차순 정렬하고 한 줄씩 print 한다

//한줄평: JS 문법만 알았으면 풀 수 있었을 것 같은데...

const readline = require("readline"); //모듈 생성
let quantity = 0;
let index=0;
let arr=[];
 
const rl = readline.createInterface({ //입출력을 위한 인터페이스 객체 생성
    input: process.stdin,
    output: process.stdout,
});
 
console.log("quantity를 입력해주세요")

rl.on("line", (line) => { //인터페이스가 내장하고있는 이벤트 실행, 문자열 타입으로 한 문자씩 받음
    if(index === 0){ //0번째 인덱스에는 입력할 값이 들어가야 함
        console.log("처음 입력한 값: " + line);
        quantity = Number(line);
        console.log(quantity + "개의 수를 입력하세요");
        index++;
    }
    else if(quantity ==! index){
        console.log(index + "번째 인덱스를 입력해주세요");
        arr[index] = Number(line); //1번째 인덱스부터 입력 값을 받는다. 
        index++;    
    }
    else if(quantity === index){
        arr.sort((a,b) => a-b); //오름차순 정렬 
        for(i=0; i<arr.length; i++) {
        console.log(arr[i]);
        rl.close(); //close가 없으면 입력을 무한히 받음
    }
  }
});

rl.on('close', () => {
    process.exit();
}) 
 




