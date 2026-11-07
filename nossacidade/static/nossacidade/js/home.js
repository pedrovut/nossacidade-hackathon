(function () {
  var cores = { critica: '#e02828', alta: '#f57c1f', media: '#f2b705', baixa: '#12a84a' };
  var el = document.getElementById('mapa');

  if (el && window.L) {
    var pontos = JSON.parse(document.getElementById('pontos-data').textContent);
    var map = L.map(el).setView([-20.4697, -54.6201], 12);

    L.tileLayer('https://basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}.png?key=cb1_54ax_1_28b1d8dbcbee0c65790edb7a', {
      maxZoom: 19,
      attribution: '© OpenStreetMap © CARTO'
    }).addTo(map);
    // Lembre-se: em reclamacao_create.html e no script interno do home.js, o final é .addTo(formMap);

    var grupo = L.featureGroup();
    pontos.forEach(function (p) {
      var m = L.circleMarker([p.lat, p.lng], { radius: 9, color: '#fff', weight: 1, fillColor: cores[p.nivel], fillOpacity: .85 });
      var a = document.createElement('a'); a.href = p.url; a.textContent = p.titulo;
      var s = document.createElement('small'); s.textContent = ' · ' + p.endereco;
      var box = document.createElement('span'); box.append(a, s);
      m.bindPopup(box); grupo.addLayer(m);
    });

    grupo.addTo(map);
    if (pontos.length) map.fitBounds(grupo.getBounds().pad(.2), { maxZoom: 16 });
  }

  // --- LÓGICA DO PAINEL LATERAL (DESKTOP) ---
  var btn = document.getElementById('btn-novo');
  var painel = document.getElementById('painel-novo');

  if (btn && painel) {
    btn.addEventListener('click', function (e) {
      if (window.matchMedia('(min-width: 900px)').matches) {
        e.preventDefault();
        painel.hidden = !painel.hidden;

        // Inicializa o mapa picker do formulário apenas quando o painel for aberto pela 1ª vez
        if (!painel.hidden && !window.formMapInitialized) {
          window.formMapInitialized = true;

          const latInput = painel.querySelector('input[name="latitude"]');
          const lngInput = painel.querySelector('input[name="longitude"]');
          const endInput = painel.querySelector('input[name="endereco"]');

          if (latInput && lngInput) {
            latInput.closest('.campo').style.display = 'none';
            lngInput.closest('.campo').style.display = 'none';
          }

          const formMapDiv = document.createElement('div');
          formMapDiv.id = 'mapa-picker-home';
          formMapDiv.style.height = '250px';
          formMapDiv.style.marginBottom = '20px';
          formMapDiv.style.borderRadius = '8px';

          endInput.closest('.campo').before(formMapDiv);

          let formMap = L.map('mapa-picker-home').setView([-20.4697, -54.6201], 13);

          L.tileLayer('https://basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}.png?key=cb1_54ax_1_28b1d8dbcbee0c65790edb7a', {
            maxZoom: 19,
            attribution: '© OpenStreetMap © CARTO'
          }).addTo(map);

          // Lembre-se: em reclamacao_create.html e no script interno do home.js, o final é .addTo(formMap);

          let formMarker = L.marker([-20.4697, -54.6201], { draggable: true }).addTo(formMap);

          function atualizarCamposHome(lat, lng) {
            latInput.value = lat;
            lngInput.value = lng;
            fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`)
              .then(res => res.json())
              .then(data => {
                if (data && data.address) {
                  let rua = data.address.road || "Endereço desconhecido";
                  let bairro = data.address.suburb || data.address.neighbourhood || "";
                  endInput.value = bairro ? `${rua}, ${bairro}` : rua;
                }
              })
              .catch(err => console.log("Erro ao buscar endereço:", err));
          }

          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function (pos) {
              const lat = pos.coords.latitude;
              const lng = pos.coords.longitude;
              formMap.setView([lat, lng], 16);
              formMarker.setLatLng([lat, lng]);
              atualizarCamposHome(lat, lng);
            });
          }

          formMarker.on('dragend', function (e) {
            const pos = formMarker.getLatLng();
            atualizarCamposHome(pos.lat, pos.lng);
          });

          formMap.on('click', function (e) {
            formMarker.setLatLng(e.latlng);
            atualizarCamposHome(e.latlng.lat, e.latlng.lng);
          });

          // Força a renderização correta do mapa que estava invisível
          setTimeout(function () {
            formMap.invalidateSize();
          }, 300);
        }
      }
    });
  }
})();