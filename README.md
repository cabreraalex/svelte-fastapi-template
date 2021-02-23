# Svelte + FastAPI Template
A simple template combining a [FastAPI](https://fastapi.tiangolo.com) backend with a [Svelte](https://svelte.dev) frontend.

Install the following:

```bash
pip3 install fastapi uvicorn
```

Install the npm dependencies:
```bash
cd ./frontend
npm i
```

And run the following for development, which watches both the backend and frontend code (unfortunately will not auto-reload when the Svelte code changes):

```bash
(uvicorn server:app --reload & (cd ./frontend; npm run dev))
```

To test out the API calls, you can go to `/docs` for a nice interactive interface.
