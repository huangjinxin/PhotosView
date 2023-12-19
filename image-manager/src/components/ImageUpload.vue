<template>
    <div class="upload-container">
      <form @submit.prevent="submitForm" class="dropzone" id="image-dropzone">
        <input type="file" name="file" @change="handleFileUpload" />
        <button type="submit">上传图片</button>
      </form>
    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    submitForm() {
      let formData = new FormData();
      formData.append('file', this.file);

      axios.post('/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
      .then(response => {
        this.$emit('image-uploaded', response.data);
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
    }
  }
}
</script>
