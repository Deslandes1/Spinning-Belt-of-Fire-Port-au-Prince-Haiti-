import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Port‑au‑Prince | Belt of Fire 2021‑2026",
    page_icon="🔥",
    layout="wide"
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown("""
    <style>
    .spin-logo {
        font-size: 60px;
        animation: spin 4s linear infinite;
        display: inline-block;
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    </style>
    <div style="text-align: center;">
        <div class="spin-logo">🔥</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("## **PORT-AU-PRINCE**")
    st.markdown("---")
    st.markdown("**Built by Gesner Deslandes** – Coder in Chief")
    st.markdown("📞 (509)-47385663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("---")
    st.markdown("### 🔥 The Belt of Fire")
    st.info("Click the voice button inside the 3D scene to hear the story of Port‑au‑Prince.")

# ---------- MAIN 3D SCENE ----------
st.markdown("<h1 style='text-align: center;'>🔥 PORT-AU-PRINCE HAITI 🔥</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>The belt spins – capital letters, fire, sparks, smoke, and a voice that tells the truth</p>", unsafe_allow_html=True)

belt_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; overflow: hidden; font-family: 'Impact', 'Arial Black', sans-serif; }
        #date-overlay {
            position: absolute;
            bottom: 30px;
            left: 0;
            right: 0;
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: #ffaa33;
            text-shadow: 0 0 20px rgba(255,100,0,0.8);
            background: rgba(0,0,0,0.5);
            padding: 10px;
            pointer-events: none;
            z-index: 100;
            font-family: monospace;
            letter-spacing: 4px;
        }
        #voiceBtn {
            position: absolute;
            bottom: 20px;
            right: 20px;
            z-index: 200;
            background: #ff4b4b;
            border: none;
            color: white;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 40px;
            cursor: pointer;
            font-size: 16px;
            transition: 0.2s;
            pointer-events: auto;
            font-family: Arial;
        }
        #voiceBtn:hover {
            background: #cc0000;
            transform: scale(1.02);
        }
        @media (max-width: 768px) {
            #date-overlay { font-size: 1.8rem; bottom: 15px; }
            #voiceBtn { padding: 8px 16px; font-size: 12px; }
        }
        #info {
            position: absolute;
            top: 20px;
            left: 20px;
            color: white;
            background: rgba(0,0,0,0.6);
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 12px;
            pointer-events: none;
            z-index: 100;
        }
    </style>
</head>
<body>
    <div id="date-overlay">🔥 2021 → 2026 🔥</div>
    <div id="info">Spinning belt of fire | Sparks & smoke | Drag to rotate</div>
    <button id="voiceBtn">🔊 AI Voice – The Story of Port‑au‑Prince</button>

    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.128.0/build/three.module.js",
                "three/addons/": "https://unpkg.com/three@0.128.0/examples/jsm/"
            }
        }
    </script>

    <script type="module">
        import * as THREE from 'three';
        import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
        import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

        // --- setup scene
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x050b1a);
        scene.fog = new THREE.FogExp2(0x050b1a, 0.02);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(3, 2, 5);
        camera.lookAt(0, 0, 0);

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.shadowMap.enabled = true;
        document.body.appendChild(renderer.domElement);

        const labelRenderer = new CSS2DRenderer();
        labelRenderer.setSize(window.innerWidth, window.innerHeight);
        labelRenderer.domElement.style.position = 'absolute';
        labelRenderer.domElement.style.top = '0px';
        labelRenderer.domElement.style.left = '0px';
        labelRenderer.domElement.style.pointerEvents = 'none';
        document.body.appendChild(labelRenderer.domElement);

        // --- controls
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.autoRotate = false;
        controls.enableZoom = true;
        controls.enablePan = true;
        controls.target.set(0, 0, 0);

        // --- lighting
        const ambient = new THREE.AmbientLight(0x222222);
        scene.add(ambient);
        const mainLight = new THREE.DirectionalLight(0xffaa66, 1);
        mainLight.position.set(2, 3, 4);
        mainLight.castShadow = true;
        scene.add(mainLight);
        const fillLight = new THREE.PointLight(0xff6600, 0.5);
        fillLight.position.set(1, 1, 2);
        scene.add(fillLight);
        const backLight = new THREE.PointLight(0xff3300, 0.3);
        backLight.position.set(-1, 1, -2);
        scene.add(backLight);

        // --- floor
        const floorMat = new THREE.MeshStandardMaterial({ color: 0x111122, roughness: 0.8, metalness: 0.2 });
        const floor = new THREE.Mesh(new THREE.PlaneGeometry(10, 10), floorMat);
        floor.rotation.x = -Math.PI/2;
        floor.position.y = -1.2;
        floor.receiveShadow = true;
        scene.add(floor);

        // --- THE BELT with CAPITAL LETTER TEXT: "PORT-AU-PRINCE HAITI"
        const canvas = document.createElement('canvas');
        canvas.width = 1024;
        canvas.height = 256;
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = '#000000';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.font = 'Bold 54px "Arial Black", "Impact"';
        ctx.fillStyle = '#ffaa33';
        ctx.shadowBlur = 0;
        const text = "PORT-AU-PRINCE HAITI  •  ";
        const textWidth = ctx.measureText(text).width;
        const repeats = Math.ceil(canvas.width / textWidth) + 1;
        for (let i = 0; i < repeats; i++) {
            ctx.fillText(text, i * textWidth, canvas.height/2 + 20);
        }
        ctx.strokeStyle = '#ff4400';
        ctx.lineWidth = 4;
        for (let i = 0; i < repeats; i++) {
            ctx.strokeText(text, i * textWidth, canvas.height/2 + 20);
        }
        const texture = new THREE.CanvasTexture(canvas);
        texture.wrapS = THREE.RepeatWrapping;
        texture.repeat.set(3, 1);

        const beltMat = new THREE.MeshStandardMaterial({ map: texture, color: 0xff6600, emissive: 0x442200, roughness: 0.3, metalness: 0.7 });
        const beltGeometry = new THREE.TorusGeometry(1.5, 0.15, 64, 200);
        const belt = new THREE.Mesh(beltGeometry, beltMat);
        belt.castShadow = true;
        scene.add(belt);
        belt.rotation.x = Math.PI / 2;
        
        const innerRingMat = new THREE.MeshStandardMaterial({ color: 0xff3300, emissive: 0x552200 });
        const innerRing = new THREE.Mesh(new THREE.TorusGeometry(1.35, 0.05, 64, 200), innerRingMat);
        innerRing.rotation.x = Math.PI / 2;
        innerRing.castShadow = true;
        scene.add(innerRing);

        // --- sparks inside belt
        const sparkCount = 800;
        const sparkGeometry = new THREE.BufferGeometry();
        const sparkPositions = new Float32Array(sparkCount * 3);
        for (let i = 0; i < sparkCount; i++) {
            const radius = 1.2 + Math.random() * 0.6;
            const angle = Math.random() * Math.PI * 2;
            sparkPositions[i*3] = Math.cos(angle) * radius;
            sparkPositions[i*3+1] = (Math.random() - 0.5) * 0.8;
            sparkPositions[i*3+2] = Math.sin(angle) * radius;
        }
        sparkGeometry.setAttribute('position', new THREE.BufferAttribute(sparkPositions, 3));
        const sparkMaterial = new THREE.PointsMaterial({ color: 0xff6600, size: 0.05, transparent: true, blending: THREE.AdditiveBlending });
        const sparks = new THREE.Points(sparkGeometry, sparkMaterial);
        scene.add(sparks);

        // --- smoke
        const smokeCount = 400;
        const smokeGeometry = new THREE.BufferGeometry();
        const smokePositions = new Float32Array(smokeCount * 3);
        const smokeVelocities = [];
        for (let i = 0; i < smokeCount; i++) {
            smokePositions[i*3] = (Math.random() - 0.5) * 5;
            smokePositions[i*3+1] = Math.random() * 3;
            smokePositions[i*3+2] = (Math.random() - 0.5) * 5;
            smokeVelocities.push({ y: 0.005 + Math.random() * 0.01, x: (Math.random()-0.5)*0.003, z: (Math.random()-0.5)*0.003 });
        }
        smokeGeometry.setAttribute('position', new THREE.BufferAttribute(smokePositions, 3));
        const smokeMaterial = new THREE.PointsMaterial({ color: 0xaaaaaa, size: 0.08, transparent: true, opacity: 0.6, blending: THREE.AdditiveBlending });
        const smoke = new THREE.Points(smokeGeometry, smokeMaterial);
        scene.add(smoke);

        // --- flame particles around belt
        const flameCount = 200;
        const flameGeometry = new THREE.BufferGeometry();
        const flamePositions = new Float32Array(flameCount * 3);
        for (let i = 0; i < flameCount; i++) {
            const angle = Math.random() * Math.PI * 2;
            const rad = 1.65;
            flamePositions[i*3] = Math.cos(angle) * rad;
            flamePositions[i*3+1] = (Math.random() - 0.5) * 0.6;
            flamePositions[i*3+2] = Math.sin(angle) * rad;
        }
        flameGeometry.setAttribute('position', new THREE.BufferAttribute(flamePositions, 3));
        const flameMaterial = new THREE.PointsMaterial({ color: 0xff4400, size: 0.04, transparent: true, blending: THREE.AdditiveBlending });
        const flames = new THREE.Points(flameGeometry, flameMaterial);
        scene.add(flames);

        // --- animation loop (belt spin, smoke rise)
        let time = 0;
        function animate() {
            requestAnimationFrame(animate);
            time += 0.02;
            
            belt.rotation.z += 0.02;   // belt spins, making the text circle
            innerRing.rotation.z += 0.025;
            sparks.rotation.y += 0.01;
            sparks.rotation.x = Math.sin(time * 0.5) * 0.1;
            flames.rotation.y -= 0.015;
            flames.rotation.x = Math.sin(time) * 0.2;
            
            // smoke rise
            const positions = smoke.geometry.attributes.position.array;
            for (let i = 0; i < smokeCount; i++) {
                let y = positions[i*3+1];
                y += smokeVelocities[i].y;
                if (y > 2.5) {
                    y = -0.5;
                    positions[i*3] = (Math.random() - 0.5) * 5;
                    positions[i*3+2] = (Math.random() - 0.5) * 5;
                } else {
                    positions[i*3] += smokeVelocities[i].x;
                    positions[i*3+2] += smokeVelocities[i].z;
                }
                positions[i*3+1] = y;
            }
            smoke.geometry.attributes.position.needsUpdate = true;
            sparks.rotation.z += 0.005;
            const intensity = 0.5 + Math.sin(time * 5) * 0.2;
            fillLight.intensity = intensity;
            
            controls.update();
            renderer.render(scene, camera);
            labelRenderer.render(scene, camera);
        }
        animate();
        
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            labelRenderer.setSize(window.innerWidth, window.innerHeight);
        });
        
        // --- AI VOICE BUTTON
        const voiceBtn = document.getElementById('voiceBtn');
        voiceBtn.addEventListener('click', () => {
            const speech = new SpeechSynthesisUtterance();
            speech.text = "Since 2021, Port‑au‑Prince Haiti has been under great pressure. Chaos has become the status. A lot of streets like Rue de la Réunion, Rue Joseph Janvier, Rue Carbone, so from Portail Léogâne to Champs‑de‑Mars, all the streets from our childhood have gone to trash, rubble and destroyed. The airport Toussaint Louverture, according to some people, has become a military base, while thousands of displaced people live in camps. It seems that the protagonists have no intention to fix Port‑au‑Prince Haiti. We Haitians, we are tired.";
            speech.lang = 'en-US';
            speech.rate = 0.9;
            speech.pitch = 1.0;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(speech);
        });
    </script>
</body>
</html>
"""

st.components.v1.html(belt_html, height=700, scrolling=False)

st.markdown("---")
st.caption("🔥 The Belt of Fire – PORT-AU-PRINCE HAITI in capital letters, spinning with fire, sparks, and smoke (2021–2026)")
