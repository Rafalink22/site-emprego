document.addEventListener("DOMContentLoaded", () => {
    const cepInput = document.getElementById("cep");
    if (cepInput) {
      cepInput.addEventListener("blur", function() {
        const cep = this.value.replace(/\D/g, ""); // Remove caracteres não numéricos
        if (cep.length === 8) {
          fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(data => {
              if (!data.erro) {
                document.getElementById("rua").value = data.logradouro || "";
                document.getElementById("bairro").value = data.bairro || "";
                document.getElementById("cidade").value = data.localidade || "";
                document.getElementById("estado").value = data.uf || "";
              } else {
                alert("CEP não encontrado!");
              }
            })
            .catch(error => console.error("Erro ao buscar o CEP:", error));
        } else {
          alert("CEP inválido!");
        }
      });
    }
  });