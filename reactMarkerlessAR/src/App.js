import React, { useRef, useState } from "react";
import "aframe";
import "aframe-particle-system-component";
import { Entity, Scene } from "aframe-react";
import { useUserMedia } from "./useUserMedia";

import "./App.scss";

const CAPTURE_OPTIONS = {
  audio: false,
  video: { facingMode: "environment" },
};

function App() {
  const videoRef = useRef();
  const [color, setColor] = useState("red");
  const mediaStream = useUserMedia(CAPTURE_OPTIONS);

  if (mediaStream && videoRef.current && !videoRef.current.srcObject) {
    videoRef.current.srcObject = mediaStream;
  }

  function handleCanPlay() {
    // calculateRatio(videoRef.current.videoHeight, videoRef.current.videoWidth);
    videoRef.current.play();
  }

  const changeColor = () => {
    const colors = ["red", "orange", "yellow", "green", "blue"];
    setColor(colors[Math.floor(Math.random() * colors.length)]);
  };

  return (
    <div className="App">
      <Scene className="ar-sceen">
        {/* <Entity primitive="a-plane" src="#groundTexture" rotation="-90 0 0" height="100" width="100"/> */}
        <Entity primitive="a-light" type="ambient" color="#445451" />
        <Entity
          primitive="a-light"
          type="point"
          intensity="2"
          position="2 4 4"
        />
        {/* <Entity primitive="a-sky" height="2048" radius="30" src="#skyTexture" theta-length="90" width="2048"/> */}
        <Entity particle-system={{ preset: "snow", particleCount: 2000 }} />
        <Entity
          text={{ value: "Hello, Markerless AR in React!", align: "center" }}
          position={{ x: 0, y: 2, z: -1 }}
        />

        <Entity
          id="box"
          geometry={{ primitive: "box" }}
          material={{ color: color, opacity: 0.6 }}
          animation__rotate={{
            property: "rotation",
            dur: 2000,
            loop: true,
            to: "360 360 360",
          }}
          animation__scale={{
            property: "scale",
            dir: "alternate",
            dur: 100,
            loop: true,
            to: "1.1 1.1 1.1",
          }}
          position={{ x: 0, y: 1, z: -3 }}
          events={{ click: changeColor }}
        >
          <Entity
            animation__scale={{
              property: "scale",
              dir: "alternate",
              dur: 100,
              loop: true,
              to: "2 2 2",
            }}
            geometry={{ primitive: "box", depth: 0.2, height: 0.2, width: 0.2 }}
            material={{ color: "#24CAFF" }}
          />
        </Entity>

        {/* <Entity primitive="a-camera">
          <Entity
            primitive="a-cursor"
            animation__click={{
              property: "scale",
              startEvents: "click",
              from: "0.1 0.1 0.1",
              to: "1 1 1",
              dur: 150,
            }}
          />
        </Entity> */}
      </Scene>
      <video
        className="video-playback"
        ref={videoRef}
        onCanPlay={handleCanPlay}
        // style={{ top: `-${offsets.y}px`, left: `-${offsets.x}px` }}
        autoPlay
        playsInline
        muted
      />
    </div>
  );
}

export default App;
