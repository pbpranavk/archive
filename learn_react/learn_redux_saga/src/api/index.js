const key = "?client_id=5f96323678d05ff0c4eb264ef184556868e303b32a2db88ecbf15746e6f25e02";

const fetchImages = async page => {
    const response = await fetch(`https://api.unsplash.com/photos/${key}&per_page=3&page=${page}`);
    const data = await response.json();
    if (response.status >= 400)
        throw new Error(data.error)
    return data;
}

const fetchImageStats = async id => {
    const response = await fetch(`https://api.unsplash.com/photos/${id}/statistics${key}`);
    const data = await response.json();
    if (response.status >= 400) {
        throw new Error(data.error)
    }
    return data;
}

export { fetchImages, fetchImageStats };