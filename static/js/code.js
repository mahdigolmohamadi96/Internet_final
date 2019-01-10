
var player = 0;

var lstdice = 0;
var lstdice2 = 0;

document.getElementById('hold').addEventListener("click",hold);
document.getElementById('roll').addEventListener("click",rolldice);

console.log('winlimite: ' ,winlim);
console.log('hold num: ' ,holdnum);
console.log('maxdice:  ' , maxdice);
console.log('dicenum :' ,dicenum);


function newgame(){
    cuurval(0);
    document.getElementById("point0").innerHTML =0;
    document.getElementById("point1").innerHTML =0;
    document.getElementById("playern0").innerHTML="player 0" ;
    document.getElementById("playern1").innerHTML="player 1";
    document.getElementById("playern1").style.color='black';
    document.getElementById("playern0").style.color='black';
    winlim = document.getElementById("lim").value;
    console.log('win limit is : ',winlim);

    player = 0;

}

function rolldice(){

    console.log('player' , player);

    num = Math.random();
    num = parseInt((num * 10)%6) + 1;
    num2 = Math.random();
    num2 = parseInt((num2 * 10)%6) + 1;
    
    if(num == 1 || num2 == 1){
        cuurval(1);
        changePlayer();
        console.log("changet from" , player); 
    }else{
        cuurval(num , num2);
    }
    console.log(num);
    dicename = '/static/picture/dice-' + num + ".png";
    dicename2 = '/static/picture/dice-' + num2 + ".png";
    console.log(dicename);
    dicePic = document.getElementById("dice-pic");
    dicePic2 = document.getElementById("dice-pic2");
    dicePic.src = dicename;
    dicePic2.src = dicename2;
    lstdice = num;
    lstdice2 = num2;
    
}

function six (){

    if(player == 0){
        point = document.getElementById("point0");
    }else if (player == 1){
        point = document.getElementById("point1");
    }
    if(player == 0){
        curr = document.getElementById("curr0");
    }else if (player == 1){
        curr = document.getElementById("curr1");
    }
    point.innerHTML = 0;
    curr.innerHTML = 0;
    changePlayer();


}

function changePlayer() {
    console.log('player' , player);
    if (player == 0){
        bg = document.getElementById("player0");
        bg.style.backgroundColor = "white";
        // consol.log(bg.style.backgroundColor);
        
        p1bg = document.getElementById("player1");
        p1bg.style.backgroundColor = "whitesmoke";
        // consol.log(p1bg.style.backgroundColor);
        lastdice =0;
        lastdice2=0;
        player = 1;
    }

    else if (player == 1){
        bg2 = document.getElementById("player1");
        bg2.style.backgroundColor = 'white';

        p1bg2 = document.getElementById("player0");
        p1bg2.style.backgroundColor = 'whitesmoke';
        player=0;
        
    }
    
}


function cuurval(val , val2){
    if(player == 0){
        curr = document.getElementById("curr0");
    }else if (player == 1){
        curr = document.getElementById("curr1");
    }
    if(val == 1 || val2 == 1){
        curr.innerHTML = 0;
        return;    
    }else if(val == 0 || val2 == 1){
        curr.innerHTML = 0;
        return;
    }else{
    curr.innerHTML = parseInt(curr.innerHTML) + val +val2;
    return;
    }
}

function hold(){
    if(player == 0){
        curr = document.getElementById("curr0");
    }else if (player == 1){
        curr = document.getElementById("curr1");
    }
    val = parseInt(curr.innerHTML);
    if(player == 0){
        point = document.getElementById("point0");
    }else if (player == 1){
        point = document.getElementById("point1");
    }
    point.innerHTML = parseInt(point.innerHTML) + val;
    cuurval(0);
    lastdice = 0;
    wincheck();
    changePlayer();
}

function wincheck(){
    if(player == 0){
        point = document.getElementById("point0");
    }else if (player == 1){
        point = document.getElementById("point1");
    }

    if(parseInt(point.innerHTML) >= winlim){
        console.log('winner is ' , player , '!!');
        if(player == 0){
            p = document.getElementById("playern0");
        }else if (player == 1){
            p = document.getElementById("playern1");
        }
        p.style.color = 'red';
        p.innerHTML = 'winer!!!'
        document.getElementById('hold').removeEventListener("click", hold);
        document.getElementById('roll').removeEventListener("click",rolldice);

    }
    
}