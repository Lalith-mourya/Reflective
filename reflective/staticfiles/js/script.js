window.addEventListener('load', () => {
    document.querySelector('.motive-text').classList.add('show');
});
function logo()
{
    const body = document.body;
    body.style.transition = "backgroundColor 0.5s";
    if(body.style.backgroundColor === 'white')
    {
        body.style.backgroundColor = 'lightblue'; 
    }
    else
    {
        body.style.backgroundColor = 'white'; 
    }
}