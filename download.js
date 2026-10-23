// Fills the download buttons with the files of the latest GitHub release and
// suggests the one for the visitor's system. Without JS the links still go
// to the release page.
(async () => {
	const box = document.querySelector('[data-repo]');
	if (!box) {
		return;
	}

	const repo = box.dataset.repo;
	// The Spanish page says it in Spanish.
	const es = document.documentElement.lang === 'es';
	const FOR = es ? 'Descargar para ' : 'Download for ';
	const FILES = {
		windows: {label: FOR + 'Windows', match: /(win-x64\.exe|windows-x86_64-setup\.exe)$/},
		macArm: {label: FOR + 'Mac (Apple Silicon)', match: /(mac-arm64|macos-arm64)\.dmg$/},
		macIntel: {label: FOR + 'Mac (Intel)', match: /(mac-x64|macos-x86_64)\.dmg$/},
		deb: {label: FOR + 'Ubuntu / Debian (.deb)', match: /\.deb$/},
		appimage: {label: FOR + 'Linux (AppImage)', match: /\.AppImage$/},
		tarball: {label: FOR + 'Linux (.tar.gz)', match: /linux-x86_64\.tar\.gz$/},
	};

	const ua = navigator.userAgent;
	let system = /Windows/.test(ua) ? 'windows'
		: /Macintosh|Mac OS X/.test(ua) ? 'macArm'
			// Browsers rarely say which Linux; most people use Ubuntu, Mint or Debian.
			: /Linux/.test(ua) ? 'deb'
					: 'windows';

	try {
		const res = await fetch(`https://api.github.com/repos/${repo}/releases/latest`);
		if (!res.ok) {
			return;
		}

		const release = await res.json();
		const urls = {};
		for (const [key, {match}] of Object.entries(FILES)) {
			urls[key] = release.assets.find(a => match.test(a.name))?.browser_download_url;
		}

		// No .deb in the release: the AppImage, or else the plain archive.
		if (system === 'deb' && !urls.deb) {
			system = urls.appimage ? 'appimage' : 'tarball';
		}

		const main = box.querySelector('.btn');
		if (urls[system]) {
			main.href = urls[system];
			main.querySelector('span').textContent = FILES[system].label;
		}

		box.querySelector('.others').replaceChildren(...Object.entries(FILES)
			.filter(([key]) => key !== system && urls[key])
			.map(([key, {label}]) => {
				const a = document.createElement('a');
				a.href = urls[key];
				a.textContent = label.replace(FOR, '');
				return a;
			}));
		const version = box.querySelector('.version');
		if (version) {
			version.textContent = `${es ? 'Versión' : 'Version'} ${release.tag_name.replace(/^v/, '')} · ${version.textContent}`;
		}
	} catch {} // offline or rate-limited: the plain links stay
})();
