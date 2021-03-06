// FROM: index.html/index.
function muestramensaje(variable) {
    let dict = JSON.parse(variable);
    
    for(const key in dict) {
        console.log(key + ": " + dict[key]);
    }
    alert(dict.dato3);
}


// Delete the tasks from the index: (index)
function delete_task(id) {
    const $btn_delete = document.getElementById(`btn-delete${id}`);
    let response = confirm("Are you sure to delete this task");
    if (response) {
        // Mandar el id de la tarea por url:
        const pagina = `http://127.0.0.1:5000/delete/task/${id}`;
        $btn_delete.setAttribute("href", pagina);
        // debugger
    }
}

// done task from the index: (index)
function done_task(id, task_done) {
    let $checkbox_done = document.getElementById(`btn-done${id}`);
    if (task_done == "False") {
        // $checkbox_done.disabled = true;
        // $checkbox_done.style.cursor = "auto";
        // $checkbox_done.checked = true;
        // Mandar el id de la tarea por url:
        let pagina = `http://127.0.0.1:5000/done/task/${id}`;
        window.location = pagina;
    }
    else {
        alert("The task has been marked as done.")
    }
    
}

// ${image.links.download}  ${image.description}  ${image.alt_description}
// http://placeimg.com/350/400/people
// FROM: account_user
if(window.location == "http://0.0.0.0:5000/user/account/ a ") {
    console.log(window.location);
    ( async () => {

        function templateImage(image) {
            // debugger
            return (
                `
                <div class="container-img" >
                    <div class="cont-general">
                        <figure class="container-photo">
                            <img id="_image" src="${image.links.download}" alt="">
                        </figure>
                        <div class="container-info">
                            <p class="name-photo">Name:<small>${image.description}</small></p>
                            <p class="description-phote">Description:<small>${image.alt_decription}</small></p>
                        </div>
                    </div>
                </div>
                `
            );
        }

        // Función para recorrer la lista que contiene las imagenes:
        function renderImageList(images, $container) {
            images.forEach((image) => {
                const HTMLString = templateImage(image);
                const elementImage = createTemplate(HTMLString);

                $container.append(elementImage);
                addEventClick(elementImage);
            });

        }

        // Add event to images:
        function addEventClick($element) {
            $element.addEventListener("click", () => {
                let $imageSrc = document.getElementById("_image");
                let url = $imageSrc.getAttribute("src");
                alert(url);
            });
        }

        // Con esta función, mandamos a traer la lista de imagenes con al api de la app:
        async function getImage(url, category, access_key1) {
            let response = await fetch(url + "&query=" + category + "&client_id=" + access_key1);
            let jsonResponse = await response.json();
            let imagesList = await jsonResponse.results;
            console.log(imagesList);
            return imagesList;
        }

        function createTemplate(HTMLString) {
            const html = document.implementation.createHTMLDocument();
            html.body.innerHTML = HTMLString;
            return html.body.children[0];
        }

        // Build the access to api unsplash:
        const access_key = "PFA40VWhEI8usL217nOGN6h7PMXJroWh_Cs9nrHU0YU";
        let category = prompt("Enter a category:");
        // Almacenamos la lista de imagenes:
        const listImages = await getImage("https://api.unsplash.com/search/photos?page=1&per_page=2", category, access_key);
        // 'https://api.unsplash.com/search/photos?query=cast&client_id=accesskey';
        // https://api.unsplash.com/search/photos?page=1&query=office


        // Obtenemos el contenedor de las imagenes:
        const $contenedor = document.getElementById("container-images");
        // Enviamos las imagenes a la función para ejecute:
        renderImageList(listImages, $contenedor);

    })();
}

