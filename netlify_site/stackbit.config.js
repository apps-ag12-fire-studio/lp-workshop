// stackbit.config.js
module.exports = {
  contentSources: [
    {
      type: 'git',
      rootPath: __dirname,
      contentDirs: ['netlify_site'],        // ou '.' se seus arquivos estão na raiz
      models: [
        {
          name: 'landing',
          type: 'page',
          urlPath: '/',                     // página inicial
          filePath: 'netlify_site/index.html',
          fields: [
            { name: 'title',   type: 'string',  label: 'Título' },
            { name: 'subtitle',type: 'string',  label: 'Subtítulo' }
          ]
        }
      ]
    }
  ]
};
