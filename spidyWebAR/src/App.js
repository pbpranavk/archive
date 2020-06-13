import React from "react";
import "aframe";
import { Entity, Scene } from "aframe-react";

function App() {
  let material = {
    shader: "flat",
    src: '/logo512.png',
    color: "black"
  }
  return (
    <Scene>
      <Entity
        geometry={{ primitive: "box" }}
        material={material}
        position={{ x: 0, y: 1.6, z: -3 }}
        animation__rotate={{
          property: "rotation",
          dur: 5000,
          loop: true,
          to: "360 360 0",
          easing: "linear",
        }}
      />
      <Entity light={{ type: "point" }} />
    </Scene>
  );
}

export default App;
