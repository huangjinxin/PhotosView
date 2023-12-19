<template>
    <div>
      <ul>
        <li v-for="image in images" :key="image.name">
          {{ image.name }}
          <button @click="deleteImage(image)">删除</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      deleteImage(image) {
        // 调用后端API删除图片
        axios.delete(`/delete-image/${image.name}`).then(response => {
          // 删除成功，发出事件或调用Vuex action来更新列表
          this.$emit('image-deleted', image);
        }).catch(error => {
          console.error('Delete failed!', error);
        });
      }
    }
  }
  </script>
  