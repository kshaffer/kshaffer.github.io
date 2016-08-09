function load_insult () {
  var animal = new Array('weasel', 'ferret', 'monkey', 'duck', 'platypus', 'chimp', 'beaver', 'ape', 'lizard', 'blowfish');
  var adjective = new Array('bearded', 'topped', 'beaked', 'footed', 'plastered', 'eating', 'breath', 'mangled', 'bottomed', 'whittled', 'splayed');
  var dirty = new Array('turd', 'poop', 'barf', 'hair', 'cheese', 'sewer', 'toilet', 'vomit', 'fungus', 'snot', 'crotch');
  var insultobject = new Array('nugget', 'burglar', ' sniffer', ' eater', 'pants', 'head', ' poacher', 'snack', ' toucher', ' licker', ' sucker', 'muppet', ' sandwich', 'burger', 'bucket');

  var random_animal = animal[Math.floor(Math.random() * animal.length)];
  var random_adjective = adjective[Math.floor(Math.random() * adjective.length)];
  var random_dirty = dirty[Math.floor(Math.random() * dirty.length)];
  var random_insultobject = insultobject[Math.floor(Math.random() * insultobject.length)];

  var insult = random_animal + '-' + random_adjective + ' ' + random_dirty + random_insultobject;

  document.getElementById('insult').innerHTML = random_animal + '-' + random_adjective + ' ' + random_dirty + random_insultobject;
}
