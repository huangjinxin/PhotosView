<script>
import 'dropzone/dist/dropzone.css';
import Dropzone from 'dropzone';

export default {
  name: 'ImageUpload',
  mounted() {
    // 直接创建Dropzone实例，无需赋值给变量
    new Dropzone("#image-dropzone", {
      url: "/upload",
      maxFilesize: 2, // 设置最大文件上传大小为2MB
      acceptedFiles: 'image/*', // 只接受图片文件
      init: function() {
        this.on("success", function(file, response) {
          // 上传成功后的回调函数
          console.log("File uploaded: ", response);
        });
      }
    });
  }
}
</script>
