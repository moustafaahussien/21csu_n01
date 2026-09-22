/* ============================================
   وحدة مهارات القرن 21 — Main JS
   Particle Network · 3D Orbit · Card Glow
   ============================================ */

(function () {
  'use strict';

  /* ---------- Theme Toggle ---------- */
  var themeToggle = document.querySelector('[data-theme-toggle]');
  var root = document.documentElement;
  var currentTheme = 'light';
  root.setAttribute('data-theme', currentTheme);
  updateThemeIcon();

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', currentTheme);
      updateThemeIcon();
    });
  }

  function updateThemeIcon() {
    if (!themeToggle) return;
    themeToggle.setAttribute('aria-label', 'Switch to ' + (currentTheme === 'dark' ? 'light' : 'dark') + ' mode');
    themeToggle.innerHTML = currentTheme === 'dark'
      ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
      : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  }

  /* ---------- Navbar Scroll ---------- */
  var navbar = document.querySelector('.navbar');
  var lastScroll = 0;
  window.addEventListener('scroll', function () {
    var scroll = window.pageYOffset;
    if (scroll > 80) navbar?.classList.add('navbar--scrolled');
    else navbar?.classList.remove('navbar--scrolled');
    if (scroll > lastScroll && scroll > 200) navbar?.classList.add('navbar--hidden');
    else navbar?.classList.remove('navbar--hidden');
    lastScroll = scroll;
  }, { passive: true });

  /* ---------- Mobile Menu ---------- */
  var navToggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
    });
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navToggle.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });
  }

  /* ---------- Animated Counters ---------- */
  var counters = document.querySelectorAll('[data-count]');
  var counterObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(function (c) { counterObserver.observe(c); });

  function animateCounter(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    if (isNaN(target)) { el.textContent = '∞'; return; }
    var duration = 1800;
    var startTime = null;
    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target).toLocaleString('en-US');
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* ---------- Gallery Lightbox ---------- */
  var galleryItems = document.querySelectorAll('.gallery-item');
  var lightbox = document.querySelector('.lightbox');
  var lightboxImg = document.querySelector('.lightbox-content img');
  galleryItems.forEach(function (item) {
    item.addEventListener('click', function () {
      var img = item.querySelector('img');
      if (img && lightbox && lightboxImg) {
        lightboxImg.src = img.src; lightboxImg.alt = img.alt || '';
        lightbox.classList.add('active');
      }
    });
  });
  if (lightbox) {
    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox || e.target.closest('.lightbox-close')) lightbox.classList.remove('active');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lightbox.classList.contains('active')) lightbox.classList.remove('active');
    });
  }

  /* ============================================
     PARTICLE NETWORK — Colorful, repels from mouse
     ============================================ */
  var canvas = document.getElementById('particleCanvas');
  if (canvas) {
    var ctx = canvas.getContext('2d');
    var particles = [];
    var mouse = { x: -1000, y: -1000, radius: 120 };
    var colors = ['#8b5cf6', '#0ea5e9', '#10b981', '#f97316', '#ec4899'];
    var particleCount = window.innerWidth < 768 ? 35 : 70;
    var maxDist = 130;

    function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resize();
    window.addEventListener('resize', function () { resize(); initParticles(); });

    function initParticles() {
      particles = [];
      for (var i = 0; i < particleCount; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          vx: (Math.random() - 0.5) * 0.5,
          vy: (Math.random() - 0.5) * 0.5,
          r: Math.random() * 2.5 + 1,
          c: colors[Math.floor(Math.random() * colors.length)],
          baseX: 0, baseY: 0
        });
        particles[i].baseX = particles[i].x;
        particles[i].baseY = particles[i].y;
      }
    }
    initParticles();

    window.addEventListener('mousemove', function (e) { mouse.x = e.clientX; mouse.y = e.clientY; });
    window.addEventListener('mouseleave', function () { mouse.x = -1000; mouse.y = -1000; });

    function drawParticles() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw connections
      for (var i = 0; i < particles.length; i++) {
        for (var j = i + 1; j < particles.length; j++) {
          var dx = particles[i].x - particles[j].x;
          var dy = particles[i].y - particles[j].y;
          var dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < maxDist) {
            var opacity = (1 - dist / maxDist) * 0.15;
            ctx.strokeStyle = 'rgba(139, 92, 246, ' + opacity + ')';
            ctx.lineWidth = 0.6;
            ctx.beginPath();
            ctx.moveTo(particles[i].x, particles[i].y);
            ctx.lineTo(particles[j].x, particles[j].y);
            ctx.stroke();
          }
        }
      }

      // Draw & update particles
      for (var k = 0; k < particles.length; k++) {
        var p = particles[k];

        // Mouse repulsion
        var mdx = p.x - mouse.x;
        var mdy = p.y - mouse.y;
        var mDist = Math.sqrt(mdx * mdx + mdy * mdy);
        if (mDist < mouse.radius) {
          var force = (mouse.radius - mDist) / mouse.radius * 2;
          p.vx += (mdx / mDist) * force * 0.3;
          p.vy += (mdy / mDist) * force * 0.3;
        }

        // Damping
        p.vx *= 0.97;
        p.vy *= 0.97;

        // Slight drift back toward base
        p.vx += (p.baseX - p.x) * 0.0008;
        p.vy += (p.baseY - p.y) * 0.0008;

        // Move
        p.x += p.vx;
        p.y += p.vy;

        // Wrap edges
        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;

        // Draw
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = p.c;
        ctx.globalAlpha = 0.5;
        ctx.fill();
        ctx.globalAlpha = 1;
      }

      if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
        requestAnimationFrame(drawParticles);
      }
    }
    drawParticles();
  }

  /* ============================================
     3D ORBITAL SYSTEM
     ============================================ */
  var orbitContainer = document.querySelector('.orbit-container');
  var orbitTilt = document.querySelector('.orbit-tilt');
  var orbitRing = document.querySelector('.orbit-ring');
  var orbitArms = document.querySelectorAll('.orbit-arm');

  if (orbitRing && orbitArms.length > 0) {
    var orbitRadius = window.innerWidth < 480 ? 110 : (window.innerWidth < 768 ? 140 : 180);
    var sphereSize = window.innerWidth < 480 ? 60 : (window.innerWidth < 768 ? 72 : 110);
    var containerSize = orbitContainer.offsetWidth;
    var center = containerSize / 2;

    // Position each arm around the circle
    orbitArms.forEach(function (arm, i) {
      var angle = (360 / orbitArms.length) * i;
      arm.style.transform = 'translate(-50%, -50%) rotate(' + angle + 'deg) translateY(-' + orbitRadius + 'px) rotate(-' + angle + 'deg)';
      arm.style.position = 'absolute';
      arm.style.top = '50%';
      arm.style.left = '50%';
    });

    // Create electric current SVG lines from center to each sphere
    var svgNS = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(svgNS, 'svg');
    svg.setAttribute('class', 'orbit-current-svg');
    svg.setAttribute('viewBox', '0 0 ' + containerSize + ' ' + containerSize);
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');

    var sphereColors = ['#ec4899', '#0ea5e9', '#f97316', '#10b981', '#8b5cf6', '#ef4444'];
    orbitArms.forEach(function (arm, i) {
      var angle = (360 / orbitArms.length) * i;
      var rad = (angle - 90) * Math.PI / 180; // -90 to start from top
      var x2 = center + orbitRadius * Math.cos(rad);
      var y2 = center + orbitRadius * Math.sin(rad);
      var color = sphereColors[i] || '#8b5cf6';

      // Glow line (wider, semi-transparent)
      var glowLine = document.createElementNS(svgNS, 'line');
      glowLine.setAttribute('x1', center);
      glowLine.setAttribute('y1', center);
      glowLine.setAttribute('x2', x2);
      glowLine.setAttribute('y2', y2);
      glowLine.setAttribute('stroke', color);
      glowLine.setAttribute('stroke-width', '4');
      glowLine.setAttribute('opacity', '0.15');
      glowLine.setAttribute('stroke-linecap', 'round');
      svg.appendChild(glowLine);

      // Main animated current line
      var line = document.createElementNS(svgNS, 'line');
      line.setAttribute('x1', center);
      line.setAttribute('y1', center);
      line.setAttribute('x2', x2);
      line.setAttribute('y2', y2);
      line.setAttribute('stroke', color);
      line.setAttribute('stroke-width', '2');
      line.setAttribute('opacity', '0.5');
      line.setAttribute('stroke-linecap', 'round');
      line.style.animationDelay = (i * 0.2) + 's';
      svg.appendChild(line);
    });
    orbitRing.insertBefore(svg, orbitRing.firstChild);

    // Mouse proximity pause
    orbitContainer.addEventListener('mouseenter', function () {
      orbitRing.classList.add('paused');
    });
    orbitContainer.addEventListener('mouseleave', function () {
      orbitRing.classList.remove('paused');
    });

    // 3D tilt with mouse
    if (orbitTilt) {
      orbitContainer.addEventListener('mousemove', function (e) {
        var rect = orbitContainer.getBoundingClientRect();
        var cx = rect.left + rect.width / 2;
        var cy = rect.top + rect.height / 2;
        var dx = (e.clientX - cx) / rect.width;
        var dy = (e.clientY - cy) / rect.height;
        orbitTilt.style.transform = 'rotateY(' + (dx * 15) + 'deg) rotateX(' + (-dy * 15) + 'deg)';
      });
      orbitContainer.addEventListener('mouseleave', function () {
        orbitTilt.style.transform = 'rotateY(0deg) rotateX(0deg)';
      });
    }
  }

  /* ============================================
     CARD MOUSE-FOLLOW GLOW
     ============================================ */
  var programCards = document.querySelectorAll('.program-card');
  programCards.forEach(function (card) {
    card.addEventListener('mousemove', function (e) {
      var rect = card.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      card.style.setProperty('--mouse-x', x + 'px');
      card.style.setProperty('--mouse-y', y + 'px');

      // 3D tilt
      var cx = rect.width / 2;
      var cy = rect.height / 2;
      var dx = (x - cx) / cx;
      var dy = (y - cy) / cy;
      card.style.transform = 'translateY(-6px) rotateX(' + (-dy * 4) + 'deg) rotateY(' + (dx * 4) + 'deg)';
    });
    card.addEventListener('mouseleave', function () {
      card.style.transform = '';
    });
  });

  /* ---------- Smooth Scroll ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;
      var target = document.querySelector(targetId);
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });

})();
