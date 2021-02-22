<script lang="ts">
  let randNumb = 0;

  function updateNumber() {
    fetch("/rand")
      .then((d) => d.text())
      .then((d) => (randNumb = parseInt(d)));
  }
</script>

<main>
  <h1>Hello Svelte + Fast.API!!!</h1>
  <p>Your random number is <span class="number">{randNumb}</span></p>
  <button on:click={updateNumber}>new number</button>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  .number {
    font-weight: 800;
    color: #ff3e00;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
