let groupClass = document.getElementsByClassName("input-group")

for (let i = 0; i < groupClass.length; i++) {
	groupClass[i].children[0].onfocus = function() {
		this.parentElement.children[1].classList.add("active");
	}

	groupClass[i].children[0].onblur = function(){
		if (this.value <= 0) {
			this.parentElement.children[1].classList.remove("active");
		}
	}
}
