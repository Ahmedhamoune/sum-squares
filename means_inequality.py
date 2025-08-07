from manim import *
import numpy as np


class MeansInequality(Scene):
    def construct(self) -> None:
        self.camera.background_color = "#223343"

        # Colors (match your previous scene)
        qm_color = RED
        am_color = MAROON_B
        gm_color = TEAL
        hm_color = BLUE_C

        # Final values used at the end of your previous scene
        a_value = 4
        b_value = 2

        # 1) Recreate final horizontal group (number line + tips + labels)
        number_line = NumberLine(
            x_range=[0, 5, 1],
            length=10,
            color=WHITE,
            include_numbers=False,
        )
        zero_label = MathTex("0", color=WHITE).scale(0.8)
        zero_label.next_to(number_line.n2p(0), DOWN, buff=0.2)

        tip_a = Triangle(color=WHITE, fill_opacity=1).scale(0.15).rotate(PI)
        tip_a.next_to(number_line.n2p(a_value), UP, buff=0.25)
        tip_b = Triangle(color=WHITE, fill_opacity=1).scale(0.15).rotate(PI)
        tip_b.next_to(number_line.n2p(b_value), UP, buff=0.25)

        label_a = MathTex("a", color=WHITE).next_to(tip_a, UP, buff=0.4)
        label_b = MathTex("b", color=WHITE).next_to(tip_b, UP, buff=0.4)

        tip_qm = (
            Triangle(color=qm_color, fill_opacity=1)
            .scale(0.1)
            .rotate(0)
            .next_to(number_line.n2p(np.sqrt((a_value**2 + b_value**2) / 2)), UP, buff=0.25)
        )
        tip_am = (
            Triangle(color=am_color, fill_opacity=1)
            .scale(0.1)
            .rotate(0)
            .next_to(number_line.n2p(0.5 * (a_value + b_value)), UP, buff=0.25)
        )
        tip_gm = (
            Triangle(color=gm_color, fill_opacity=1)
            .scale(0.1)
            .rotate(0)
            .next_to(number_line.n2p(np.sqrt(a_value * b_value)), UP, buff=0.25)
        )
        tip_hm = (
            Triangle(color=hm_color, fill_opacity=1)
            .scale(0.1)
            .rotate(0)
            .next_to(number_line.n2p((2 * a_value * b_value) / (a_value + b_value)), UP, buff=0.25)
        )

        axis_group_final = VGroup(
            number_line,
            tip_a,
            tip_b,
            label_a,
            label_b,
            zero_label,
            tip_qm,
            tip_am,
            tip_gm,
            tip_hm,
        )

        self.play(
            Create(number_line),
            FadeIn(zero_label),
            FadeIn(tip_a), FadeIn(label_a),
            FadeIn(tip_b), FadeIn(label_b),
            FadeIn(tip_qm), FadeIn(tip_am), FadeIn(tip_gm), FadeIn(tip_hm),
        )
        self.wait(0.6)

        # 2) Transform to inequality chain: b < HM < GM < AM < QM < a
        b_tok = MathTex("b", color=WHITE)
        hm_tok = MathTex("\\mathrm{HM}", color=hm_color)
        gm_tok = MathTex("\\mathrm{GM}", color=gm_color)
        am_tok = MathTex("\\mathrm{AM}", color=am_color)
        qm_tok = MathTex("\\mathrm{QM}", color=qm_color)
        a_tok = MathTex("a", color=WHITE)

        lt1 = MathTex("\\leq", color=WHITE)
        lt2 = MathTex("\\leq", color=WHITE)
        lt3 = MathTex("\\leq", color=WHITE)
        lt4 = MathTex("\\leq", color=WHITE)
        lt5 = MathTex("\\leq", color=WHITE)

        chain = VGroup(
            b_tok, lt1, hm_tok, lt2, gm_tok, lt3, am_tok, lt4, qm_tok, lt5, a_tok
        ).arrange(RIGHT, buff=0.6).scale(1.2).move_to(ORIGIN)

        # Place tokens at sources to get a clean morph
        b_tok.move_to(label_b)
        hm_tok.move_to(tip_hm)
        gm_tok.move_to(tip_gm)
        am_tok.move_to(tip_am)
        qm_tok.move_to(tip_qm)
        a_tok.move_to(label_a)

        for lt in [lt1, lt2, lt3, lt4, lt5]:
            lt.set_opacity(0)

        self.play(
            ReplacementTransform(label_b, b_tok),
            ReplacementTransform(tip_hm, hm_tok),
            ReplacementTransform(tip_gm, gm_tok),
            ReplacementTransform(tip_am, am_tok),
            ReplacementTransform(tip_qm, qm_tok),
            ReplacementTransform(label_a, a_tok),
            FadeOut(tip_a),
            FadeOut(tip_b),
            FadeOut(number_line),
            FadeOut(zero_label),
        )

        # Reveal signs
        self.play(
            LaggedStart(*[FadeIn(lt) for lt in [lt1, lt2, lt3, lt4, lt5]], lag_ratio=0.1),
            run_time=0.6,
        )

        # Neaten the chain into place
        chain.generate_target()
        chain.target.arrange(RIGHT, buff=0.6).scale(1.2).move_to(ORIGIN)
        self.play(MoveToTarget(chain), run_time=1.0)
        self.wait(0.6)

        # 3) Replace each mean with its formula (keep colors)
        hm_formula = MathTex("\\frac{2ab}{a+b}", color=hm_color)
        gm_formula = MathTex("\\sqrt{ab}", color=gm_color)
        am_formula = MathTex("\\frac{a+b}{2}", color=am_color)
        qm_formula = MathTex("\\sqrt{\\frac{a^{2}+b^{2}}{2}}", color=qm_color)

        hm_formula.move_to(hm_tok)
        gm_formula.move_to(gm_tok)
        am_formula.move_to(am_tok)
        qm_formula.move_to(qm_tok)

        self.play(
            ReplacementTransform(hm_tok, hm_formula),
            ReplacementTransform(gm_tok, gm_formula),
            ReplacementTransform(am_tok, am_formula),
            ReplacementTransform(qm_tok, qm_formula),
            run_time=1.2,
        )
        self.wait(0.6)

        # 4) Replace them with their squares (keep inequality signs)
        hm_sq = MathTex("\\left(\\frac{2ab}{a+b}\\right)^{2}", color=hm_color)
        gm_sq = MathTex("ab", color=gm_color)
        am_sq = MathTex("\\frac{(a+b)^{2}}{4}", color=am_color)
        qm_sq = MathTex("\\frac{a^{2}+b^{2}}{2}", color=qm_color)

        hm_sq.move_to(hm_formula)
        gm_sq.move_to(gm_formula)
        am_sq.move_to(am_formula)
        qm_sq.move_to(qm_formula)

        self.play(
            ReplacementTransform(hm_formula, hm_sq),
            ReplacementTransform(gm_formula, gm_sq),
            ReplacementTransform(am_formula, am_sq),
            ReplacementTransform(qm_formula, qm_sq),
            run_time=1.2,
        )
        self.wait(2.0)