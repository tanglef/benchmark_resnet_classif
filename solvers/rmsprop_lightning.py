from benchopt import safe_import_context


with safe_import_context() as import_ctx:
    from torch.optim import RMSprop

LightningSolver = import_ctx.import_from('lightning_solver', 'LightningSolver')


class Solver(LightningSolver):
    """RMSPROP solver"""
    name = 'RMSPROP-lightning'

    # any parameter defined here is accessible as a class attribute
    parameters = {
        'lr': [1e-3],
        'rho': [0.99, 0.9],
        'momentum': [0, 0.9],
        'coupled_weight_decay': [0.0, 1e-4, 0.02],
        **LightningSolver.parameters
    }

    def set_objective(self, **kwargs):
        super().set_objective(**kwargs)
        self.optimizer_klass = RMSprop
        self.optimizer_kwargs = dict(
            lr=self.lr,
            momentum=self.momentum,
            alpha=self.rho,
            weight_decay=self.coupled_weight_decay,
        )
