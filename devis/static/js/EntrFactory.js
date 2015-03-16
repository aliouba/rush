angular.module("NewEntr", [ ]).factory("newentreprise",function(){
	//Pour fonctionner , ces méthodes aurons besoins d'un modèle qu'on va cacher
	//Tout ce qui suit est privé
	var entrs = [
		{"entr":{id:1,"name":"SG","siret":"1234567","adesse":"12 Rue Mongenot Paris"},"conf":{"type":"parPlant","parGuyot":true,"parDep":true,"parPente":true}},
		{"entr":{id:2,"name":"CA","siret":"2547896","adesse":"1 Rue Paris 75001"},"conf":{"type":"parSup","parGuyot":true,"parDep":true,"parPente":true}}
	];
	//Tout ce qui est dans le return est public
	//les variables privées au dessus ne seront utilisabales que par les fonctions publiques ( ci-dessous ) dans le return
	return{

		getEntrs : function(){
			return entrs;
		},
		getEntr : function(idEntr){
			for ( var i = 0; i < entrs.length; i++ ){
				var entr = entrs[i].;
				if( entr.id == idEntr ){
					return  entr ; 
				}

			}
			return null;

		},
		setEntr : function(entr){
			var idEntr = entrs.length;
			entr.id = idEntr + 1;
			allEntrs = this.getEntrs();
			allEntrs.push(entr);
		}
	}
})