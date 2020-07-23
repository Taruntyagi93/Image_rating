<template>
  <span class="main">
    <h1 class="heading">The Image Rating App</h1>

    <b-row cols="12" class="imageRow">
      <b-col cols="1"> </b-col>

      <b-col cols="4" class="imageCol">
        <img
          class="imageIteam"
          thumbnail
          fluid
          src="../assets/groot.jpg"
          alt="Image 1"
        />
        <b-button
          class="counterButton"
          v-on:click="decrease"
          value="counter1"
          variant="outline-danger"
          >&#8722;
        </b-button>
        <span class="counter">{{ counter1 }}</span>
        <b-button
          class="counterButton"
          value="counter1"
          v-on:click="increase"
          variant="outline-success"
        >
          &#43;</b-button
        >
      </b-col>

      <b-col cols="2"> </b-col>

      <b-col cols="4" class="imageCol">
        <img
          class="imageIteam"
          thumbnail
          fluid
          src="../assets/Flower.jpg"
          alt="Image 2"
        />
        <b-button
          class="counterButton"
          value="counter2"
          v-on:click="decrease"
          variant="outline-danger"
          >&#8722;</b-button
        >
        <span class="counter">{{ counter2 }}</span>
        <b-button
          class="counterButton"
          value="counter2"
          v-on:click="increase"
          variant="outline-success"
        >
          &#43;</b-button
        >
      </b-col>
      <b-col cols="1"> </b-col>
    </b-row>

    <b-row cols="12" class="imageRow">
      <b-col cols="1"> </b-col>

      <b-col cols="4" class="imageCol">
        <img
          class="imageIteam"
          thumbnail
          fluid
          src="../assets/Pond.jpg"
          alt="Image 1"
        />
        <b-button
          class="counterButton"
          value="counter3"
          v-on:click="decrease"
          variant="outline-danger"
          >&#8722;</b-button
        >
        <span class="counter">{{ counter3 }}</span>
        <b-button
          class="counterButton"
          value="counter3"
          v-on:click="increase"
          variant="outline-success"
        >
          &#43;</b-button
        >
      </b-col>

      <b-col cols="2"> </b-col>

      <b-col cols="4" class="imageCol">
        <img
          class="imageIteam"
          thumbnail
          fluid
          src="../assets/road.jpg"
          alt="Image 2"
        />
        <b-button
          class="counterButton"
          value="counter4"
          v-on:click="decrease"
          variant="outline-danger"
          >&#8722;</b-button
        >
        <span class="counter">{{ counter4 }}</span>
        <b-button
          class="counterButton"
          value="counter4"
          v-on:click="increase"
          variant="outline-success"
        >
          &#43;</b-button
        >
      </b-col>

      <b-col cols="1"> </b-col>
    </b-row>

    <b-button class="saveButton" v-on:click="submit" variant="primary">
      Save Values</b-button
    >
  </span>
</template>

<script>
import axios from "axios";
export default {
  name: "Images",
  data: function() {
    return {
      counter1: 0,
      counter2: 0,
      counter3: 0,
      counter4: 0,
    };
  },
  methods: {
    decrease: function(e) {
      if (e.target.value == "counter1") {
        this.counter1 -= 1;
      } else if (e.target.value == "counter2") {
        this.counter2 -= 1;
      } else if (e.target.value == "counter3") {
        this.counter3 -= 1;
      } else if (e.target.value == "counter4") {
        this.counter4 -= 1;
      }
    },
    increase: function(e) {
      if (e.target.value == "counter1") {
        this.counter1 += 1;
      } else if (e.target.value == "counter2") {
        this.counter2 += 1;
      } else if (e.target.value == "counter3") {
        this.counter3 += 1;
      } else if (e.target.value == "counter4") {
        this.counter4 += 1;
      }
    },
    getstate: function() {
      let result = [];
      axios.get("http://127.0.0.1:5000/counter").then((response) => {
        result = response.data;
        console.log(result);
        this.counter1 = result[0].counter;
        this.counter2 = result[1].counter;
        this.counter3 = result[2].counter;
        this.counter4 = result[3].counter;
      });
    },
    submit: function() {
      let data = [];
      data.push(
        { name: "counter1", counter: this.counter1 },
        { name: "counter2", counter: this.counter2 },
        { name: "counter3", counter: this.counter3 },
        { name: "counter4", counter: this.counter4 }
      );

      axios
        .post("http://127.0.0.1:5000/updateCounter", data)
        .then((response) => {
          console.log(response);
        });
    },
  },
  created() {
    this.getstate();
  },
};
</script>

<style scoped lang="less">
.heading {
  margin-bottom: 20px;
  padding: 0px;
  margin-top: 0px;
}
.main {
  padding: 0px;
  margin: 0px;
}
.imageRow {
  padding: 0px;
  margin: 0px;
}
.imageCol {
  margin: 0px;
}
.counter {
  font-family: sans-serif;
  font-size: 20px;
}
.imageIteam {
  padding: 0px;
  margin: 0px;
  width: 500px;
  height: 400px;
  border-radius: 40px;
  box-shadow: 5px 5px 5px 5px #888888;
  margin-bottom: 7px;
}
.counterButton {
  padding: 2px;
  margin: 10px;
  width: 3vw;
  height: 4vh;
}
</style>
