var player = 0;

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

// console.log('winlimite: ', winlim);
// console.log('hold num: ', holdnum);
// console.log('maxdice:  ', maxdice);
// console.log('dicenum :', dicenum);

update();

function jsonHandler(resp, act) {

    winlim = resp.max_score;
    if (act === 'roll-dice') rolldice(resp.dices);
    // if (act === 'hold')// hold();
    if (act === ' ') update_page();

    var holdnum = resp.hold;
    if (resp.turn!==0) {
        player = 0;
    } else player = 1;
    console.log('turn is:' , resp.turn , 'turrrrn isss:' , player);
    changePlayer();
    dicenum = resp.dice_count;
    p1_current = resp.player1_current;
    p1_total = resp.player1_total;
    p2_current = resp.player2_current;
    p2_total = resp.player2_total;
    winner = resp.winner;


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

function newgame() {
    cuurval(0);
    document.getElementById("point0").innerHTML = 0;
    document.getElementById("point1").innerHTML = 0;
    document.getElementById("playern0").innerHTML = "player 0";
    document.getElementById("playern1").innerHTML = "player 1";
    document.getElementById("playern1").style.color = 'black';
    document.getElementById("playern0").style.color = 'black';
    winlim = document.getElementById("lim").value;
    console.log('win limit is : ', winlim);

    player = 0;

}

function rolldice(dices) {

    console.log(dices);
    num = dices[0];
    num2 = dices[1];
    num3 = dices[2];
    num4 = dices[3];

    console.log('player', player);

    if (num == 1 || num2 == 1) {
        cuurval(1);
        changePlayer();
        console.log("changet from", player);
    } else {
        cuurval(num, num2);
    }
    console.log(num2);
    dicename = '../static/picture/dice-' + num + ".png";
    dicename2 = '../static/picture/dice-' + num2 + ".png";
    console.log(dicename);
    dicePic = document.getElementById("dice-pic");
    dicePic2 = document.getElementById("dice-pic2");
    dicePic.src = dicename;
    dicePic2.src = dicename2;
    lstdice = num;
    lstdice2 = num2;

}

function six() {

    if (player == 0) {
        point = document.getElementById("point0");
    } else if (player == 1) {
        point = document.getElementById("point1");
    }
    if (player == 0) {
        curr = document.getElementById("curr0");
    } else if (player == 1) {
        curr = document.getElementById("curr1");
    }
    point.innerHTML = 0;
    curr.innerHTML = 0;
    changePlayer();


}

function changePlayer() {
    console.log('player', player);
    if (player == 0) {
        bg = document.getElementById("player0");
        bg.style.backgroundColor = "white";
        // consol.log(bg.style.backgroundColor);

        p1bg = document.getElementById("player1");
        p1bg.style.backgroundColor = "whitesmoke";

        // consol.log(p1bg.style.backgroundColor);
        lastdice = 0;
        lastdice2 = 0;

        player = 1;

        $('#wait').hide();
        $('#keys').show();
    } else if (player == 1) {
        bg2 = document.getElementById("player1");
        bg2.style.backgroundColor = 'white';

        p1bg2 = document.getElementById("player0");
        p1bg2.style.backgroundColor = 'whitesmoke';

        player = 0;
        $('#wait').show();
        $('#keys').hide();

    }

}


function cuurval(val, val2) {
    if (player === 0) {
        curr = document.getElementById("curr0");
    } else if (player === 1) {
        curr = document.getElementById("curr1");
    }
    if (val == 1 || val2 == 1) {
        curr.innerHTML = 0;
        return;
    } else if (val == 0 || val2 == 1) {
        curr.innerHTML = 0;
        return;
    } else {
        curr.innerHTML = parseInt(curr.innerHTML) + val + val2;
        return;
    }
}

function hold() {
    if (player == 0) {
        curr = document.getElementById("curr0");
    } else if (player == 1) {
        curr = document.getElementById("curr1");
    }
    val = parseInt(curr.innerHTML);
    if (player == 0) {
        point = document.getElementById("point0");
    } else if (player == 1) {
        point = document.getElementById("point1");
    }
    point.innerHTML = parseInt(point.innerHTML) + val;
    cuurval(0);
    lastdice = 0;
    wincheck();
    changePlayer();
}

function wincheck() {
    if (player == 0) {
        point = document.getElementById("point0");
    } else if (player == 1) {
        point = document.getElementById("point1");
    }

    if (parseInt(point.innerHTML) >= winlim) {
        console.log('winner is ', player, '!!');
        if (player == 0) {
            p = document.getElementById("playern0");
        } else if (player == 1) {
            p = document.getElementById("playern1");
        }
        p.style.color = 'red';
        p.innerHTML = 'winer!!!'
        document.getElementById('hold').removeEventListener("click", hold);
        document.getElementById('roll').removeEventListener("click", rolldice);

    }

}