// var player = 0;
var player;
var lstdice = 0;
var lstdice2 = 0;
var p1_current;
var p1_total;
var p2_current;
var p2_total;


document.getElementById('hold').addEventListener("click", function () {
    getresp("hold")
});
document.getElementById('roll').addEventListener("click", function () {
    getresp("roll-dice")
});


update();

// jsonHandler();
function jsonHandler(resp, act) {
    console.log(resp);


    if (resp.dice_count === 1) {
        $('#dice-pic2').hide();
        $('#dice-pic3').hide();
        $('#dice-pic4').hide();
    } else if (resp.dice_count === 2) {
        $('#dice-pic3').hide();
        $('#dice-pic4').hide();
    } else if (resp.dice_count === 3) {
        $('#dice-pic4').hide();
    }


    wincheck(resp);
    if (resp.turn_id === resp.user_id) {
        player = 1;
        handleWait(player);
    } else {
        player = 0;
        handleWait(player);
    }

    winlim = resp.max_score;
    if (act === 'roll-dice') rolldice(resp.dices);
    // if (act === 'hold')// hold();
    if (act === ' ') update_page();

    var holdnum = resp.hold;


    console.log('user id is : ', resp.user_id);

    console.log('turn is:', resp.turn, 'turrrrn isss:', player);
    // changePlayer();
    holdnums = resp.hold;
    // console.log(holdnums);
    dicenum = resp.dice_count;
    p1_current = resp.player1_current;
    p1_total = resp.player1_total;
    p2_current = resp.player2_current;
    p2_total = resp.player2_total;
    winner = resp.winner;


}


function handleWait(player) {
    if (player === 1) {
        $('#wait').hide();
        $('#keys').show();
        bg = document.getElementById("player0");
        bg.style.backgroundColor = "white";
        p1bg = document.getElementById("player1");
        p1bg.style.backgroundColor = "whitesmoke";
    } else if (player === 0) {
        $('#wait').show();
        $('#keys').hide();
        bg = document.getElementById("player1");
        bg.style.backgroundColor = "white";
        p1bg = document.getElementById("player0");
        p1bg.style.backgroundColor = "whitesmoke";
    }
}

function update_page() {
    document.getElementById("curr0").innerHTML = p1_current;
    document.getElementById("curr1").innerHTML = p2_current;
    document.getElementById("point0").innerHTML = p1_total;
    document.getElementById("point1").innerHTML = p2_total;
}

function getresp(act = " ") {
    $.ajax({
        url: '/playGame/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            game_id: gameid,
            action: act
        }),
        success: function (data) {
            jsonHandler(JSON.parse(data), act);
        }
    })
}

function update() {
    getresp();
    setTimeout(update, 2000);
}


// function newgame() {
//     cuurval(0);
//     document.getElementById("point0").innerHTML = 0;
//     document.getElementById("point1").innerHTML = 0;
//     document.getElementById("playern0").innerHTML = "player 0";
//     document.getElementById("playern1").innerHTML = "player 1";
//     document.getElementById("playern1").style.color = 'black';
//     document.getElementById("playern0").style.color = 'black';
//     winlim = document.getElementById("lim").value;
//     console.log('win limit is : ', winlim);
//
//     player = 0;
//
// }

function rolldice(dices) {

    console.log(dices);
    num = dices[0];
    num2 = dices[1];
    num3 = dices[2];
    num4 = dices[3];

    if (num in holdnums || num2 in holdnums || num3 in holdnums || num4 in holdnums) {

    } else {

        console.log('player', player);
        console.log(num2);
        dicename = '../static/picture/dice-' + num + ".png";
        dicename2 = '../static/picture/dice-' + num2 + ".png";
        console.log(dicename);
        dicePic = document.getElementById("dice-pic");
        dicePic2 = document.getElementById("dice-pic2");
        dicePic.src = dicename;
        dicePic2.src = dicename2;
    }

}

// function six() {
//
//     if (player == 0) {
//         point = document.getElementById("point0");
//     } else if (player == 1) {
//         point = document.getElementById("point1");
//     }
//     if (player == 0) {
//         curr = document.getElementById("curr0");
//     } else if (player == 1) {
//         curr = document.getElementById("curr1");
//     }
//     point.innerHTML = 0;
//     curr.innerHTML = 0;
//     // changePlayer();
//
//
// }

// function changePlayer() {
//     console.log('player', player);
//     if (player == 0) {
//         bg = document.getElementById("player0");
//         bg.style.backgroundColor = "white";
//         // consol.log(bg.style.backgroundColor);
//
//         p1bg = document.getElementById("player1");
//         p1bg.style.backgroundColor = "whitesmoke";
//
//         // consol.log(p1bg.style.backgroundColor);
//         lastdice = 0;
//         lastdice2 = 0;
//
//         player = 1;
//         //
//         // $('#wait').show();
//         // $('#keys').hide();
//     } else if (player == 1) {
//         bg2 = document.getElementById("player1");
//         bg2.style.backgroundColor = 'white';
//
//         p1bg2 = document.getElementById("player0");
//         p1bg2.style.backgroundColor = 'whitesmoke';
//
//         player = 0;
//         // $('#wait').hide();
//         // $('#keys').show();
//
//     }

// }


// function cuurval(val, val2) {
//
//
//     curr1 = document.getElementById("curr0");
//     curr1.innerHTML = val;
//     curr2 = document.getElementById("curr1");
//     curr2.innerHTML = val2;
//
//
// }

// function hold() {
//     if (player == 0) {
//         curr = document.getElementById("curr0");
//     } else if (player == 1) {
//         curr = document.getElementById("curr1");
//     }
//     val = parseInt(curr.innerHTML);
//     if (player == 0) {
//         point = document.getElementById("point0");
//     } else if (player == 1) {
//         point = document.getElementById("point1");
//     }
//     point.innerHTML = parseInt(point.innerHTML) + val;
//     // cuurval(0);
//     lastdice = 0;
//     wincheck();
//     // changePlayer();
// }

function wincheck(resp) {
    if (resp.winner === resp.user_id) {
        p = document.getElementById("playern1");
        p.style.color = 'red';
        p.innerHTML = 'winer!!!';
        document.getElementById('hold').removeEventListener("click", hold);
        document.getElementById('roll').removeEventListener("click", rolldice);
    } else if (resp.winner !== null) {
        console.log('winner is : ', winner);
        p = document.getElementById("playern0");
        p.style.color = 'red';
        p.innerHTML = 'winer!!!';
        document.getElementById('hold').removeEventListener("click", hold);
        document.getElementById('roll').removeEventListener("click", rolldice);
    }


}