<template>
    <div class="no-access">
        <p>Nie masz dostępu do tej strony :(</p>
    </div>
</template>

<script>
export default {
  name: 'NoAccess'
}
</script>

<style scoped>
.no-access {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 50vh;
}

.no-access p {
    font-size: 200%;
}
</style>
