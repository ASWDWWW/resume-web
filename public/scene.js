import * as THREE from 'three';

const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function initChrome() {
    const bar = document.getElementById('scrollProgress');
    const links = document.querySelectorAll('a.nav-link');
    const sections = [...document.querySelectorAll('main section[id]')];

    function onScroll() {
        const max = document.documentElement.scrollHeight - window.innerHeight;
        const progress = max > 0 ? window.scrollY / max : 0;
        if (bar) bar.style.transform = 'scaleX(' + progress + ')';

        const marker = window.scrollY + 160;
        let current = '';
        sections.forEach((section) => {
            if (section.offsetTop <= marker) current = section.id;
        });
        links.forEach((link) => {
            link.classList.toggle('is-active', link.getAttribute('href') === '#' + current);
        });
    }

    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
}

function nearestEdges(positions, count) {
    const edges = [];
    const seen = new Set();
    for (let i = 0; i < count; i++) {
        const dists = [];
        for (let j = 0; j < count; j++) {
            if (i === j) continue;
            const dx = positions[i * 3] - positions[j * 3];
            const dy = positions[i * 3 + 1] - positions[j * 3 + 1];
            const dz = positions[i * 3 + 2] - positions[j * 3 + 2];
            dists.push([j, dx * dx + dy * dy + dz * dz]);
        }
        dists.sort((a, b) => a[1] - b[1]);
        for (let n = 0; n < 2; n++) {
            if (dists[n][1] > 42) continue;
            const j = dists[n][0];
            const a = Math.min(i, j);
            const b = Math.max(i, j);
            const key = a + ':' + b;
            if (seen.has(key)) continue;
            seen.add(key);
            edges.push(
                positions[a * 3], positions[a * 3 + 1], positions[a * 3 + 2],
                positions[b * 3], positions[b * 3 + 1], positions[b * 3 + 2]
            );
        }
    }
    return edges;
}

function initScene() {
    const canvas = document.getElementById('webgl');
    if (!canvas) return;

    const renderer = new THREE.WebGLRenderer({
        canvas,
        antialias: true,
        alpha: true,
        powerPreference: 'high-performance',
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
    renderer.setClearColor(0x000000, 0);

    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x070b14, 0.055);

    const camera = new THREE.PerspectiveCamera(40, 1, 0.1, 80);
    camera.position.set(0, 0, 18);

    const count = window.innerWidth < 768 ? 64 : 120;
    const positions = new Float32Array(count * 3);
    const colors = new Float32Array(count * 3);
    const palette = [
        new THREE.Color('#5eead4'),
        new THREE.Color('#93c5fd'),
        new THREE.Color('#c4b5fd'),
    ];
    for (let i = 0; i < count; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 26;
        positions[i * 3 + 1] = (Math.random() - 0.5) * 14;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 10;
        const color = palette[i % palette.length];
        colors[i * 3] = color.r;
        colors[i * 3 + 1] = color.g;
        colors[i * 3 + 2] = color.b;
    }

    const pointGeo = new THREE.BufferGeometry();
    pointGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    pointGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    const points = new THREE.Points(pointGeo, new THREE.PointsMaterial({
        size: 0.055,
        vertexColors: true,
        transparent: true,
        opacity: 0.8,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
    }));

    const lineGeo = new THREE.BufferGeometry();
    lineGeo.setAttribute('position', new THREE.Float32BufferAttribute(nearestEdges(positions, count), 3));
    const lines = new THREE.LineSegments(lineGeo, new THREE.LineBasicMaterial({
        color: 0x9bd8d0,
        transparent: true,
        opacity: 0.16,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
    }));

    const field = new THREE.Group();
    field.add(points);
    field.add(lines);
    scene.add(field);

    const sculpture = new THREE.Group();
    const ico = new THREE.LineSegments(
        new THREE.EdgesGeometry(new THREE.IcosahedronGeometry(1.35, 1)),
        new THREE.LineBasicMaterial({ color: 0xc4b5fd, transparent: true, opacity: 0.55 })
    );
    const ring = new THREE.Mesh(
        new THREE.TorusGeometry(2.15, 0.012, 12, 96),
        new THREE.MeshBasicMaterial({ color: 0x5eead4, transparent: true, opacity: 0.4 })
    );
    const ringB = new THREE.Mesh(
        new THREE.TorusGeometry(2.7, 0.008, 12, 80),
        new THREE.MeshBasicMaterial({ color: 0x93c5fd, transparent: true, opacity: 0.28 })
    );
    ringB.rotation.x = Math.PI / 2.6;
    sculpture.add(ico, ring, ringB);
    scene.add(sculpture);

    let pointerX = 0;
    let pointerY = 0;
    let scrollP = 0;
    window.addEventListener('pointermove', (event) => {
        pointerX = (event.clientX / window.innerWidth - 0.5) * 2;
        pointerY = (event.clientY / window.innerHeight - 0.5) * 2;
    }, { passive: true });

    function readScroll() {
        const max = document.documentElement.scrollHeight - window.innerHeight;
        scrollP = max > 0 ? window.scrollY / max : 0;
    }
    window.addEventListener('scroll', readScroll, { passive: true });
    readScroll();

    function layout() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        camera.aspect = width / Math.max(height, 1);
        camera.updateProjectionMatrix();
        renderer.setSize(width, height, false);
        const wide = width >= 768;
        sculpture.visible = wide;
        sculpture.position.set(wide ? 5.1 : 0, wide ? 0.35 : 0, -1.5);
        sculpture.scale.setScalar(wide ? 1 : 0.7);
    }
    window.addEventListener('resize', layout);
    layout();

    const clock = new THREE.Clock();
    let playing = false;
    let raf = 0;

    function frame() {
        if (!playing) return;
        const t = clock.getElapsedTime();
        field.rotation.y = t * 0.03 + pointerX * 0.06;
        field.rotation.x = pointerY * 0.03 + scrollP * 0.18;
        sculpture.rotation.y = t * 0.16 + pointerX * 0.12;
        sculpture.rotation.x = Math.sin(t * 0.2) * 0.12 + pointerY * 0.05;
        ring.rotation.z = t * 0.07;
        ringB.rotation.z = -t * 0.05;
        camera.position.x += (pointerX * 0.45 - camera.position.x) * 0.04;
        camera.position.y += (-pointerY * 0.25 - scrollP * 0.8 - camera.position.y) * 0.04;
        camera.lookAt(0, 0, 0);
        renderer.render(scene, camera);
        raf = requestAnimationFrame(frame);
    }

    function start() {
        if (playing) return;
        playing = true;
        clock.getDelta();
        raf = requestAnimationFrame(frame);
    }

    function stop() {
        playing = false;
        cancelAnimationFrame(raf);
    }

    document.addEventListener('visibilitychange', () => {
        if (document.hidden) stop();
        else start();
    });

    start();
}

initChrome();
if (!reduced) {
    try {
        initScene();
    } catch (err) {
        const canvas = document.getElementById('webgl');
        if (canvas) canvas.remove();
    }
}
