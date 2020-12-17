function sayHello() {
    $.get('/hello').then(response => {
        console.log(response);
    });
}

sayHello();