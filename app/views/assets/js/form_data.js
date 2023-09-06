const travel_form = document.getElementById('data-form');
travel_form.addEventListener('submit', event=>{
    event.preventDefault();
    const formData = new FormData(travel_form);
    const data = Object.fromEntries(formData);
    fetch('http://127.0.0.1:8000/traveler',{
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body:data
    })
})


    
