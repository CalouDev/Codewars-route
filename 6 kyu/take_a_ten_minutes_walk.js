function direction(chr, newVal) {
    for (let j = 0; j < value.length; j++) {
         if (value[j] == chr) {
            value.splice(j, 1);
            return 0;
         }
    }
    value.push(newVal);
}

function isValidWalk(walk) {
    if (walk.length != 10) {
        return false;
    }

    value = [];

    for (let i = 0; i < walk.length; i++) {
        switch(walk[i]) {
            case 'n':
                direction('s', walk[i]);
                break;
            case 'e':
                direction('w', walk[i]);
                break;
            case 's':
                direction('n', walk[i]);
                break;
            case 'w':
                direction('e', walk[i]);
                break;
        }
    }
    if (value.length) {
        return false;
    }
    return true;
}
